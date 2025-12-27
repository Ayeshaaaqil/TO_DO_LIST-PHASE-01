"""
Command-line interface for the Todo In-Memory Python Console App.

This module defines the TodoCLI class which provides a simple text-based menu
interface for users to interact with the todo list.
"""

from .todo_list import TodoList
from typing import Optional


class TodoCLI:
    """
    Provides a command-line interface for interacting with the TodoList.
    
    Attributes:
        todo_list (TodoList): The TodoList instance to manage tasks
    """
    
    def __init__(self):
        """
        Initializes the CLI with a new TodoList instance.
        """
        self.todo_list = TodoList()

    def display_menu(self):
        """
        Displays the main menu options to the user.
        """
        print("\n--- Todo List Menu ---")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete/incomplete")
        print("6. Exit")
        print("----------------------")

    def get_user_choice(self) -> str:
        """
        Gets the user's menu choice.
        
        Returns:
            str: The user's menu choice
        """
        return input("Enter your choice (1-6): ").strip()

    def add_task(self):
        """
        Handles adding a new task based on user input.
        """
        print("\n--- Add a New Task ---")
        title = input("Enter task title: ").strip()
        
        if not title:
            print("Error: Task title cannot be empty.")
            return
        
        description = input("Enter task description (optional): ").strip()
        
        try:
            task = self.todo_list.add_task(title, description)
            print(f"Task added successfully with ID {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def list_tasks(self):
        """
        Handles listing all tasks.
        """
        print("\n--- All Tasks ---")
        tasks = self.todo_list.list_tasks()
        
        if not tasks:
            print("No tasks found.")
            return
        
        # Print header
        print(f"{'ID':<4} {'Status':<8} {'Title':<30} {'Description'}")
        print("-" * 70)
        
        # Print each task
        for task in tasks:
            status = "[✓]" if task.completed else "[ ]"
            # Truncate title if too long
            title = task.title
            if len(title) > 30:
                title = title[:27] + "..."
            # Truncate description if too long
            description = task.description if task.description else ""
            if len(description) > 30:
                description = description[:27] + "..."
            print(f"{task.id:<4} {status:<8} {title:<30} {description}")

    def update_task(self):
        """
        Handles updating an existing task based on user input.
        """
        print("\n--- Update a Task ---")
        
        try:
            task_id = int(input("Enter task ID to update: ").strip())
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        # Check if task exists
        task = self.todo_list.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        print(f"Current task: {task.title}")
        print(f"Current description: {task.description}")
        
        new_title = input("Enter new title (or press Enter to keep current): ").strip()
        new_description = input("Enter new description (or press Enter to keep current): ").strip()
        
        # Prepare update parameters
        title_update = new_title if new_title else None
        description_update = new_description if new_description else None
        
        try:
            updated = self.todo_list.update_task(task_id, title_update, description_update)
            if updated:
                print("Task updated successfully.")
            else:
                print("Task update failed.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task(self):
        """
        Handles deleting a task based on user input.
        """
        print("\n--- Delete a Task ---")
        
        try:
            task_id = int(input("Enter task ID to delete: ").strip())
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        # Confirm deletion
        task = self.todo_list.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("Deletion cancelled.")
            return
        
        deleted = self.todo_list.delete_task(task_id)
        if deleted:
            print("Task deleted successfully.")
        else:
            print("Task deletion failed.")

    def mark_task(self):
        """
        Handles marking a task as complete/incomplete based on user input.
        """
        print("\n--- Mark Task Complete/Incomplete ---")
        
        try:
            task_id = int(input("Enter task ID to mark: ").strip())
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        # Check if task exists
        task = self.todo_list.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        toggled = self.todo_list.mark_task(task_id)
        if toggled:
            status = "completed" if task.completed else "incomplete"
            print(f"Task marked as {status}.")
        else:
            print("Task status toggle failed.")

    def run(self):
        """
        Runs the main application loop.
        """
        print("Welcome to the Todo List Application!")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")