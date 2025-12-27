"""
Unit tests for the Task model in the Todo In-Memory Python Console App.
"""

import pytest
from src.todo.task import Task


class TestTask:
    """Test cases for the Task dataclass."""
    
    def test_task_creation_with_valid_data(self):
        """Test creating a Task with valid data."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=False)
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
    
    def test_task_creation_with_defaults(self):
        """Test creating a Task with default values."""
        task = Task(id=1, title="Test Task")
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.completed is False
    
    def test_task_creation_with_completed_true(self):
        """Test creating a Task with completed status as True."""
        task = Task(id=1, title="Test Task", completed=True)
        
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.completed is True
    
    def test_task_title_cannot_be_empty(self):
        """Test that creating a Task with an empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(id=1, title="")
    
    def test_task_title_cannot_be_whitespace_only(self):
        """Test that creating a Task with whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(id=1, title="   ")
    
    def test_task_repr(self):
        """Test the string representation of a Task."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=True)
        expected_repr = "Task(id=1, title='Test Task', description='Test Description', completed=True)"
        
        assert repr(task) == expected_repr