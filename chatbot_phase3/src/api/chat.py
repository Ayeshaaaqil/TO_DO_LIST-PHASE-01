"""
Chat API Endpoint

This module implements the stateless chat API endpoint that accepts
user messages and returns AI-generated responses for todo management.
"""
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
import json
from ..api.auth_middleware import get_current_user
from ..database.database import get_session
from ..agents.todo_agent import TodoAgent


router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    conversation_id: str
    message_id: Optional[str] = None


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    current_user_id: UUID = Depends(get_current_user)
):
    """
    Process a user's natural language message and return an AI-generated response for todo management.

    This endpoint:
    1. Authenticates the user
    2. Retrieves conversation history from database
    3. Sends user message to AI agent
    4. Agent invokes MCP tools as needed
    5. Receives response from agent
    6. Stores new messages in conversation history
    7. Returns response to user
    """
    try:
        # Process the message with the AI agent
        agent = TodoAgent()
        agent_response = await agent.process_message(
            request.message,
            str(current_user_id),
            request.conversation_id or str(UUID(int=1))
        )

        return ChatResponse(
            response=agent_response["response"],
            conversation_id=agent_response["conversation_id"],
            message_id=None
        )
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Handle any other errors
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred processing your request: {str(e)}"
        )


@router.get("/chat/config")
async def chat_config():
    """Return configuration information about the chat service."""
    return {
        "status": "available",
        "features": ["text_processing", "conversation_tracking", "todo_management"],
        "version": "1.0.0"
    }