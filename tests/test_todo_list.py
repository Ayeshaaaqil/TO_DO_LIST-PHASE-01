"""
Unit tests for the TodoList model in the Todo In-Memory Python Console App.
"""

import pytest
from src.todo.todo_list import TodoList
from src.todo.task import Task


class TestTodoList:
    """Test cases for the TodoList class."""
    
    def test_initialization(self):
        """Test that TodoList initializes with empty tasks and next_id of 1."""
        todo_list = TodoList()
        
        assert todo_list.tasks == []
        assert todo_list.next_id == 1
    
    def test_add_task_with_valid_data(self):
        """Test adding a task with valid data."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task", "Test Description")
        
        assert len(todo_list.tasks) == 1
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
        assert todo_list.next_id == 2
    
    def test_add_task_with_only_title(self):
        """Test adding a task with only a title."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task")
        
        assert len(todo_list.tasks) == 1
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.completed is False
    
    def test_add_task_assigns_unique_ids(self):
        """Test that each added task gets a unique ID."""
        todo_list = TodoList()
        
        task1 = todo_list.add_task("Task 1")
        task2 = todo_list.add_task("Task 2")
        task3 = todo_list.add_task("Task 3")
        
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
        assert len(todo_list.tasks) == 3
    
    def test_add_task_title_cannot_be_empty(self):
        """Test that adding a task with an empty title raises ValueError."""
        todo_list = TodoList()
        
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            todo_list.add_task("")
    
    def test_add_task_title_cannot_be_whitespace_only(self):
        """Test that adding a task with whitespace-only title raises ValueError."""
        todo_list = TodoList()
        
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            todo_list.add_task("   ")
    
    def test_list_tasks_empty_list(self):
        """Test listing tasks when the list is empty."""
        todo_list = TodoList()
        tasks = todo_list.list_tasks()
        
        assert tasks == []
    
    def test_list_tasks_sorted_by_id(self):
        """Test that tasks are returned sorted by ID in ascending order."""
        todo_list = TodoList()
        
        # Add tasks in reverse order to test sorting
        todo_list.add_task("Task 3")
        todo_list.add_task("Task 1")  # This will have ID 2
        todo_list.add_task("Task 2")  # This will have ID 3
        
        tasks = todo_list.list_tasks()
        
        assert len(tasks) == 3
        assert tasks[0].id == 1  # Task 1
        assert tasks[1].id == 2  # Task 2 (originally "Task 1")
        assert tasks[2].id == 3  # Task 3 (originally "Task 2")
    
    def test_get_task_by_id_exists(self):
        """Test getting a task that exists."""
        todo_list = TodoList()
        added_task = todo_list.add_task("Test Task")
        
        retrieved_task = todo_list.get_task_by_id(added_task.id)
        
        assert retrieved_task is not None
        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title
    
    def test_get_task_by_id_not_exists(self):
        """Test getting a task that does not exist."""
        todo_list = TodoList()
        
        retrieved_task = todo_list.get_task_by_id(999)
        
        assert retrieved_task is None
    
    def test_update_task_title(self):
        """Test updating a task's title."""
        todo_list = TodoList()
        task = todo_list.add_task("Original Title")
        
        updated = todo_list.update_task(task.id, title="New Title")
        
        assert updated is True
        assert task.title == "New Title"
    
    def test_update_task_description(self):
        """Test updating a task's description."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Title", "Original Description")
        
        updated = todo_list.update_task(task.id, description="New Description")
        
        assert updated is True
        assert task.description == "New Description"
    
    def test_update_task_both_fields(self):
        """Test updating both title and description."""
        todo_list = TodoList()
        task = todo_list.add_task("Original Title", "Original Description")
        
        updated = todo_list.update_task(task.id, title="New Title", description="New Description")
        
        assert updated is True
        assert task.title == "New Title"
        assert task.description == "New Description"
    
    def test_update_task_title_cannot_be_empty(self):
        """Test that updating a task with an empty title raises ValueError."""
        todo_list = TodoList()
        task = todo_list.add_task("Original Title")
        
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            todo_list.update_task(task.id, title="")
    
    def test_update_task_not_found(self):
        """Test updating a task that does not exist."""
        todo_list = TodoList()
        
        updated = todo_list.update_task(999, title="New Title")
        
        assert updated is False
    
    def test_delete_task_exists(self):
        """Test deleting a task that exists."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task")
        
        deleted = todo_list.delete_task(task.id)
        
        assert deleted is True
        assert len(todo_list.tasks) == 0
    
    def test_delete_task_not_exists(self):
        """Test deleting a task that does not exist."""
        todo_list = TodoList()
        
        deleted = todo_list.delete_task(999)
        
        assert deleted is False
    
    def test_delete_task_removes_correct_task(self):
        """Test that deleting a task removes only the specified task."""
        todo_list = TodoList()
        task1 = todo_list.add_task("Task 1")
        task2 = todo_list.add_task("Task 2")
        task3 = todo_list.add_task("Task 3")
        
        deleted = todo_list.delete_task(task2.id)
        
        assert deleted is True
        assert len(todo_list.tasks) == 2
        assert todo_list.get_task_by_id(task1.id) is not None
        assert todo_list.get_task_by_id(task2.id) is None
        assert todo_list.get_task_by_id(task3.id) is not None
    
    def test_mark_task_toggle_to_completed(self):
        """Test marking a pending task as completed."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task")
        
        toggled = todo_list.mark_task(task.id)
        
        assert toggled is True
        assert task.completed is True
    
    def test_mark_task_toggle_to_pending(self):
        """Test marking a completed task as pending."""
        todo_list = TodoList()
        task = todo_list.add_task("Test Task")
        # First mark as completed
        todo_list.mark_task(task.id)
        
        # Now mark as pending
        toggled = todo_list.mark_task(task.id)
        
        assert toggled is True
        assert task.completed is False
    
    def test_mark_task_not_found(self):
        """Test marking a task that does not exist."""
        todo_list = TodoList()
        
        toggled = todo_list.mark_task(999)
        
        assert toggled is False