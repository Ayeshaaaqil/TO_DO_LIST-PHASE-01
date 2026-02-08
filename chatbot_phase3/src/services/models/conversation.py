from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import uuid
from datetime import datetime
from enum import Enum


class MessageType(str, Enum):
    user = "user"
    assistant = "assistant"


class ConversationBase(SQLModel):
    title: str
    user_id: uuid.UUID


class Conversation(ConversationBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to messages
    messages: list["ConversationMessage"] = Relationship(back_populates="conversation")


class ConversationMessageBase(SQLModel):
    role: MessageType
    content: str
    conversation_id: uuid.UUID


class ConversationMessage(ConversationMessageBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to conversation
    conversation: Optional[Conversation] = Relationship(back_populates="messages")