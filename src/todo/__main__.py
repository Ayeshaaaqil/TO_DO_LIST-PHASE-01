"""
Main entry point for the Todo In-Memory Python Console App.

This module provides the main function to run the application when executed
directly or via `python -m todo`.
"""

from .cli import TodoCLI


def main():
    """
    Main function to start the Todo CLI application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()