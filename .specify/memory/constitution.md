# The Evolution of Todo - Project Constitution

## Project Overview

"The Evolution of Todo" is a simple in-memory command-line todo application implemented in Python. This is Phase I of the project, focusing on building a solid foundation with core functionality. The application will provide users with a command-line interface to manage their tasks efficiently without the complexity of persistence mechanisms.

The primary goal of this phase is to establish a clean, maintainable codebase that follows Spec-Driven Development (SDD) principles. The application will support basic todo operations including adding, listing, updating, deleting, and marking tasks as complete/incomplete.

## Core Values

1. **Spec-Driven Development First**: Every feature MUST start from a written specification in the specs/ folder. Never write code without an approved spec. Use Spec-Kit Plus workflow strictly: constitution → specify → plan → tasks → implement.

2. **Clean Code and Readability**: Favor simple, readable code over clever solutions. Follow PEP 8 strictly. Use meaningful variable/function names. Keep functions short (<50 lines where possible). Add docstrings to all modules, classes, and functions.

3. **Proper Project Structure**: Organize the codebase according to a standard Python project layout with clear separation of concerns.

4. **Simplicity over Features**: Prioritize simple, working solutions over complex feature-rich implementations.

5. **Error Handling**: Design with robust error handling to provide a good user experience even when inputs are invalid.

## Technical Principles

1. **In-Memory Only**: All tasks stored in a list/dict in memory. No persistence to file or database in this phase.

2. **CLI Interface**: Implement a simple text-based menu or command loop. Provide user-friendly prompts and handle invalid inputs gracefully.

3. **Modular Design**: Structure code to be modular and testable with clear separation of concerns.

4. **PEP 8 Compliance**: Strictly follow Python's style guide for consistency and readability.

5. **No External Dependencies**: Use only the Python standard library for core logic (optional: use rich or typer for better CLI if it improves UX without complexity).

## Required Features

1. **Add Task**: Support adding tasks with a required title and optional description.

2. **List/View Tasks**: Display all tasks showing ID, title, description, and status (pending/completed) with clear indicators.

3. **Update Task**: Allow updating tasks by ID, supporting updates to title or description.

4. **Delete Task**: Enable deletion of tasks by ID.

5. **Mark Complete/Incomplete**: Allow toggling task status by ID.

6. **Error Handling**: Validate inputs and handle edge cases (empty list, invalid ID, etc.) without crashing.

## Project Structure

The project follows a standard Python package structure:

```
todo/
├── src/
│   └── todo/
│       ├── __init__.py
│       ├── main.py          # Entry point with CLI loop
│       ├── task.py          # Task model
│       └── todo_list.py     # In-memory storage and operations
├── tests/
│   ├── test_task.py
│   └── test_todo_list.py
├── specs/
│   └── <feature-name>/
│       ├── spec.md
│       ├── plan.md
│       └── tasks.md
├── .specify/
│   ├── memory/
│   │   └── constitution.md  # This file
│   ├── scripts/
│   └── templates/
├── history/
│   ├── prompts/
│   └── adr/
├── README.md
├── CLAUDE.md
├── pyproject.toml
└── .gitignore
```

## Tooling and Documentation

1. **Development Environment**: Use uv for virtual environment and dependencies management.

2. **Python Version**: Target Python 3.13+ for modern language features and performance.

3. **Testing Framework**: Use pytest for unit tests with good coverage of operations.

4. **Documentation Requirements**:
   - README.md: Setup instructions (uv usage), how to run, example commands
   - CLAUDE.md: Detailed instructions for continuing work with Claude Code and Spec-Kit Plus
   - specs/: Keep full specs history for all features

5. **Spec Management**: Maintain complete specifications in specs/ folder with spec.md, plan.md, and tasks.md for each feature.

## General Rules and Guidelines

1. **Confirmation for Changes**: Always ask for confirmation before major changes to ensure alignment with project goals.

2. **Modular Code**: Prefer modular, testable code over monolithic implementations.

3. **No Unnecessary Boilerplate**: Include only code that serves a clear purpose.

4. **Graceful Error Handling**: Handle invalid inputs and edge cases gracefully without crashing the application.

5. **User Experience**: Prioritize clear, understandable error messages and user prompts.

6. **Validation**: Implement input validation to ensure data integrity and prevent runtime errors.

7. **Testing**: Write comprehensive unit tests for all core functions to ensure reliability and prevent regressions.

## Implementation Workflow

This project follows the Spec-Kit Plus methodology:

1. **Constitution**: Establish project principles (this document)
2. **Specify**: Create detailed feature specifications in specs/
3. **Plan**: Design the architecture for each feature
4. **Tasks**: Break down implementation into testable tasks
5. **Implement**: Write code following the approved specifications

This workflow ensures that all development is specification-driven and that the project maintains consistency with its core values throughout its evolution.