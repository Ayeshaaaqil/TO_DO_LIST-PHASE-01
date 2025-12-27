# Development Instructions for Todo Console App

## Project Overview

This is a simple in-memory command-line todo application implemented in Python. The project follows Spec-Driven Development (SDD) principles with a clean, modular architecture.

## Project Structure

```
todo/
├── src/
│   └── todo/
│       ├── __init__.py
│       ├── task.py          # Task model definition
│       ├── todo_list.py     # In-memory storage and operations
│       ├── cli.py           # Command-line interface
│       └── __main__.py      # Entry point for python -m todo
├── tests/
│   ├── test_task.py         # Tests for Task model
│   ├── test_todo_list.py    # Tests for TodoList operations
│   └── test_cli.py          # Tests for CLI functionality
├── specs/
│   └── 001-todo-console-app/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
└── pyproject.toml           # Project configuration
```

## Spec-Kit Plus Workflow

This project follows the Spec-Kit Plus methodology:

1. **Constitution**: Project principles are in `.specify/memory/constitution.md`
2. **Specify**: Feature specifications in `specs/` folder
3. **Plan**: Architecture designs in `specs/*/plan.md`
4. **Tasks**: Implementation tasks in `specs/*/tasks.md`
5. **Implement**: Code implementation following the approved specifications

## Development Commands

- Run the application: `python -m todo`
- Run tests: `pytest`
- Run with coverage: `pytest --cov=todo`
- Install dependencies: `uv sync` or `pip install -e .`

## Code Structure

- `task.py`: Defines the Task data model with id, title, description, and completed status
- `todo_list.py`: Manages the in-memory collection of tasks and provides all CRUD operations
- `cli.py`: Provides the command-line interface with menu options and user interaction
- `__main__.py`: Entry point for running the application with `python -m todo`

## Testing Strategy

- Unit tests for each component in the tests/ directory
- Test coverage target: 95% for core logic
- Tests for happy paths, error paths, and edge cases
- Integration tests for CLI functionality

## Contributing

1. Follow the SDD workflow: create specs first, then plan, then implement
2. Write tests for new functionality
3. Maintain 95%+ test coverage for core logic
4. Follow PEP 8 style guidelines
5. Add docstrings to all modules, classes, and functions