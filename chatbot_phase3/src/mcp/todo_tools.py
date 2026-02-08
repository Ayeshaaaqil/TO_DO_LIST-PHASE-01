"""
MCP (Model Context Protocol) Tools for Todo Management

This module provides tools that the AI agent can use to perform
todo-related operations based on natural language requests.
"""

from typing import Dict, Any, Optional
import uuid
from sqlmodel import Session, select
from ..services.models.todo import Todo
from ..services.models.user import User


class TodoMCPTools:
    """Class containing MCP tools for todo management operations."""
    
    @staticmethod
    def create_todo(session: Session, user_id: str, title: str, description: str = "") -> Dict[str, Any]:
        """
        Create a new todo for the user.
        
        Args:
            session: Database session
            user_id: ID of the user creating the todo
            title: Title of the new todo
            description: Description of the new todo
            
        Returns:
            Dictionary with the created todo information
        """
        from uuid import UUID
        
        todo = Todo(
            title=title,
            description=description,
            user_id=UUID(user_id)
        )
        session.add(todo)
        session.commit()
        session.refresh(todo)
        
        return {
            "id": str(todo.id),
            "title": todo.title,
            "description": todo.description,
            "is_completed": todo.is_completed,
            "message": f"Todo '{title}' created successfully"
        }
    
    @staticmethod
    def get_user_todos(session: Session, user_id: str) -> list:
        """
        Get all todos for a specific user.
        
        Args:
            session: Database session
            user_id: ID of the user
            
        Returns:
            List of todos for the user
        """
        from uuid import UUID
        
        user_uuid = UUID(user_id)
        todos = session.exec(select(Todo).where(Todo.user_id == user_uuid)).all()
        
        return [{
            "id": str(todo.id),
            "title": todo.title,
            "description": todo.description,
            "is_completed": todo.is_completed
        } for todo in todos]
    
    @staticmethod
    def update_todo(
        session: Session, 
        user_id: str, 
        todo_id: str, 
        title: Optional[str] = None, 
        description: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update an existing todo for the user.
        
        Args:
            session: Database session
            user_id: ID of the user
            todo_id: ID of the todo to update
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            Dictionary with the updated todo information
        """
        from uuid import UUID
        
        user_uuid = UUID(user_id)
        todo_uuid = UUID(todo_id)
        
        todo = session.get(Todo, todo_uuid)
        if not todo or todo.user_id != user_uuid:
            raise ValueError("Todo not found or access denied")
        
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
            
        session.add(todo)
        session.commit()
        session.refresh(todo)
        
        return {
            "id": str(todo.id),
            "title": todo.title,
            "description": todo.description,
            "is_completed": todo.is_completed,
            "message": f"Todo '{todo.title}' updated successfully"
        }
    
    @staticmethod
    def toggle_todo_completion(session: Session, user_id: str, todo_id: str) -> Dict[str, Any]:
        """
        Toggle the completion status of a todo.
        
        Args:
            session: Database session
            user_id: ID of the user
            todo_id: ID of the todo to toggle
            
        Returns:
            Dictionary with the updated todo information
        """
        from uuid import UUID
        
        user_uuid = UUID(user_id)
        todo_uuid = UUID(todo_id)
        
        todo = session.get(Todo, todo_uuid)
        if not todo or todo.user_id != user_uuid:
            raise ValueError("Todo not found or access denied")
        
        todo.is_completed = not todo.is_completed
        session.add(todo)
        session.commit()
        session.refresh(todo)
        
        status = "completed" if todo.is_completed else "marked incomplete"
        return {
            "id": str(todo.id),
            "title": todo.title,
            "description": todo.description,
            "is_completed": todo.is_completed,
            "message": f"Todo '{todo.title}' has been {status}"
        }
    
    @staticmethod
    def delete_todo(session: Session, user_id: str, todo_id: str) -> Dict[str, Any]:
        """
        Delete a todo for the user.
        
        Args:
            session: Database session
            user_id: ID of the user
            todo_id: ID of the todo to delete
            
        Returns:
            Dictionary with deletion confirmation
        """
        from uuid import UUID
        
        user_uuid = UUID(user_id)
        todo_uuid = UUID(todo_id)
        
        todo = session.get(Todo, todo_uuid)
        if not todo or todo.user_id != user_uuid:
            raise ValueError("Todo not found or access denied")
        
        title = todo.title
        session.delete(todo)
        session.commit()
        
        return {
            "message": f"Todo '{title}' deleted successfully"
        }