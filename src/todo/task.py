"""
Task model for the Todo In-Memory Python Console App.

This module defines the Task dataclass which represents a single to-do item
with id, title, description, and completed status.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single to-do item with id, title, description, and completed status.
    
    Attributes:
        id (int): Unique identifier for the task
        title (str): Title of the task (required)
        description (str): Description of the task (optional)
        completed (bool): Status of the task (pending or completed)
    """
    
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """
        Validates that the title is not empty after initialization.
        
        Raises:
            ValueError: If the title is empty or contains only whitespace
        """
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")
    
    def __repr__(self):
        """
        Returns a string representation of the Task object.
        
        Returns:
            str: String representation of the Task
        """
        status_indicator = "✓" if self.completed else " "
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', completed={self.completed})"