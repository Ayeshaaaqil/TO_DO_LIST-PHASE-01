"""
TodoList model for the Todo In-Memory Python Console App.

This module defines the TodoList class which manages a collection of Task objects
and provides methods for all CRUD operations.
"""

from typing import List, Optional
from .task import Task


class TodoList:
    """
    Manages a collection of Task objects in memory and provides methods for all CRUD operations.
    
    Attributes:
        tasks (List[Task]): List of Task objects
        next_id (int): The next available ID for new tasks
    """
    
    def __init__(self):
        """
        Initializes an empty TodoList with next_id starting at 1.
        """
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Adds a new task to the list with a unique ID and pending status.
        
        Args:
            title (str): Title of the task (required)
            description (str): Description of the task (optional)
            
        Returns:
            Task: The newly created Task object
            
        Raises:
            ValueError: If the title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(id=self.next_id, title=title.strip(), description=description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self) -> List[Task]:
        """
        Returns all tasks sorted by ID in ascending order.
        
        Returns:
            List[Task]: List of all Task objects sorted by ID
        """
        return sorted(self.tasks, key=lambda task: task.id)

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a task by its ID.
        
        Args:
            task_id (int): ID of the task to retrieve
            
        Returns:
            Optional[Task]: The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Updates an existing task's title and/or description.
        
        Args:
            task_id (int): ID of the task to update
            title (Optional[str]): New title for the task (optional)
            description (Optional[str]): New description for the task (optional)
            
        Returns:
            bool: True if the task was updated, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()
        
        if description is not None:
            task.description = description.strip()
        
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task by its ID.
        
        Args:
            task_id (int): ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        return True

    def mark_task(self, task_id: int) -> bool:
        """
        Toggles the completion status of a task.
        
        Args:
            task_id (int): ID of the task to mark
            
        Returns:
            bool: True if the task status was toggled, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.completed = not task.completed
        return True