"""
Unit tests for the CLI interface in the Todo In-Memory Python Console App.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.todo.cli import TodoCLI


class TestTodoCLI:
    """Test cases for the TodoCLI class."""
    
    def setup_method(self):
        """Set up a fresh TodoCLI instance for each test."""
        self.cli = TodoCLI()
    
    def test_initialization(self):
        """Test that TodoCLI initializes with a TodoList instance."""
        assert self.cli.todo_list is not None
        assert hasattr(self.cli.todo_list, 'add_task')
        assert hasattr(self.cli.todo_list, 'list_tasks')
    
    @patch('builtins.input', side_effect=['Test Title', 'Test Description'])
    @patch('builtins.print')
    def test_add_task_valid_input(self, mock_print, mock_input):
        """Test adding a task with valid input."""
        self.cli.add_task()
        
        # Check that the task was added
        tasks = self.cli.todo_list.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Test Title"
        assert tasks[0].description == "Test Description"
        assert tasks[0].completed is False
    
    @patch('builtins.input', side_effect=['', 'Test Description'])
    @patch('builtins.print')
    def test_add_task_empty_title(self, mock_print, mock_input):
        """Test adding a task with empty title shows error."""
        self.cli.add_task()
        
        # Check that no task was added
        tasks = self.cli.todo_list.list_tasks()
        assert len(tasks) == 0
        
        # Verify error message was printed
        mock_print.assert_called()
        error_printed = any("Error: Task title cannot be empty" in str(call) for call in mock_print.call_args_list)
        assert error_printed
    
    @patch('builtins.print')
    def test_list_tasks_empty_list(self, mock_print):
        """Test listing tasks when the list is empty."""
        self.cli.list_tasks()
        
        # Verify appropriate message was printed
        mock_print.assert_any_call("No tasks found.")
    
    @patch('builtins.print')
    def test_list_tasks_with_tasks(self, mock_print):
        """Test listing tasks when the list has tasks."""
        # Add some tasks
        self.cli.todo_list.add_task("Task 1", "Description 1")
        self.cli.todo_list.add_task("Task 2", "Description 2")
        
        self.cli.list_tasks()
        
        # Verify that tasks were printed
        calls_made = [str(call) for call in mock_print.call_args_list]
        task_printed = any("Task 1" in call for call in calls_made)
        assert task_printed
    
    @patch('builtins.input', side_effect=['1', 'Updated Title', 'Updated Description'])
    @patch('builtins.print')
    def test_update_task_valid_input(self, mock_print, mock_input):
        """Test updating a task with valid input."""
        # Add a task first
        task = self.cli.todo_list.add_task("Original Title", "Original Description")
        
        self.cli.update_task()
        
        # Check that the task was updated
        updated_task = self.cli.todo_list.get_task_by_id(task.id)
        assert updated_task.title == "Updated Title"
        assert updated_task.description == "Updated Description"
    
    @patch('builtins.input', side_effect=['999', 'New Title', 'New Description'])  # Non-existent ID
    @patch('builtins.print')
    def test_update_task_not_found(self, mock_print, mock_input):
        """Test updating a task that doesn't exist."""
        self.cli.update_task()
        
        # Verify error message was printed
        mock_print.assert_any_call("Error: Task with ID 999 not found.")
    
    @patch('builtins.input', side_effect=['1', 'y'])  # Confirm deletion
    @patch('builtins.print')
    def test_delete_task_valid_input(self, mock_print, mock_input):
        """Test deleting a task with valid input."""
        # Add a task first
        task = self.cli.todo_list.add_task("Task to Delete")
        
        self.cli.delete_task()
        
        # Check that the task was deleted
        deleted_task = self.cli.todo_list.get_task_by_id(task.id)
        assert deleted_task is None
    
    @patch('builtins.input', side_effect=['999', 'y'])  # Non-existent ID
    @patch('builtins.print')
    def test_delete_task_not_found(self, mock_print, mock_input):
        """Test deleting a task that doesn't exist."""
        self.cli.delete_task()
        
        # Verify error message was printed
        mock_print.assert_any_call("Error: Task with ID 999 not found.")
    
    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_mark_task_valid_input(self, mock_print, mock_input):
        """Test marking a task with valid input."""
        # Add a task first
        task = self.cli.todo_list.add_task("Task to Mark")
        
        self.cli.mark_task()
        
        # Check that the task status was toggled
        marked_task = self.cli.todo_list.get_task_by_id(task.id)
        assert marked_task.completed is True
    
    @patch('builtins.input', side_effect=['999'])  # Non-existent ID
    @patch('builtins.print')
    def test_mark_task_not_found(self, mock_print, mock_input):
        """Test marking a task that doesn't exist."""
        self.cli.mark_task()
        
        # Verify error message was printed
        mock_print.assert_any_call("Error: Task with ID 999 not found.")