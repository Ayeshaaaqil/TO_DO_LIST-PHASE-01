from sqlmodel import Session, select
from typing import Optional
from uuid import UUID
from .models.conversation import Conversation, ConversationMessage
from datetime import datetime


class ConversationService:
    @staticmethod
    def create_conversation(session: Session, user_id: UUID, title: str) -> Conversation:
        conversation = Conversation(
            user_id=user_id,
            title=title
        )
        session.add(conversation)
        session.commit()
        session.refresh(conversation)
        return conversation

    @staticmethod
    def get_conversation_by_id(session: Session, conversation_id: UUID) -> Optional[Conversation]:
        return session.get(Conversation, conversation_id)

    @staticmethod
    def add_message_to_conversation(
        session: Session, 
        conversation_id: UUID, 
        role: str, 
        content: str
    ) -> ConversationMessage:
        message = ConversationMessage(
            conversation_id=conversation_id,
            role=role,
            content=content
        )
        session.add(message)
        session.commit()
        session.refresh(message)
        return message