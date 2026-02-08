from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import uuid
from datetime import datetime
from uuid import UUID


class TodoBase(SQLModel):
    title: str
    description: Optional[str] = Field(default="")
    is_completed: bool = Field(default=False)


class Todo(TodoBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationship to user
    user: Optional["User"] = Relationship(back_populates="todos")


# Add the relationship to the User model
from .user import User
User.todos = Relationship(back_populates="todo")