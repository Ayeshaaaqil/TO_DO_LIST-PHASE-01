# Feature Tasks: Todo In-Memory Python Console App

**Feature**: Todo In-Memory Python Console App
**Branch**: `001-todo-console-app`
**Created**: 2025-01-04
**Status**: Ready for Implementation

## Dependencies

- User Story 8 (Task model) must be completed before User Stories 1-7
- User Story 6 (CLI menu) is required for all other user stories to be accessible
- User Story 2 (List tasks) is needed to verify other operations

## Parallel Execution Examples

- User Story 3 (Update) and User Story 4 (Delete) can be implemented in parallel after User Story 8
- User Story 1 (Add) and User Story 5 (Mark complete) can be implemented in parallel after User Story 8
- All test files can be created in parallel after their respective implementation files

## Implementation Strategy

- MVP: Implement User Story 8 (Task model) + User Story 1 (Add task) + User Story 2 (List tasks) + User Story 6 (CLI menu)
- Incremental delivery: Add one user story at a time, ensuring each is fully functional before moving to the next
- Test-driven approach: Write tests for each component as it's implemented

---

## Phase 1: Setup

- [X] T001 Create project structure per implementation plan in src/todo/
- [X] T002 Create tests directory structure for test files
- [X] T003 Initialize pyproject.toml with project metadata and dependencies
- [X] T004 Create README.md with project overview and setup instructions
- [X] T005 Create CLAUDE.md with development instructions
- [X] T006 Create .gitignore with appropriate Python patterns

## Phase 2: Foundational Components

- [X] T007 [P] Create src/todo/__init__.py with proper exports
- [X] T008 [P] Create src/todo/task.py with Task dataclass definition
- [X] T009 [P] Create src/todo/todo_list.py with TodoList class skeleton
- [X] T010 [P] Create src/todo/cli.py with TodoCLI class skeleton
- [X] T011 [P] Create src/todo/__main__.py with main application entry point
- [X] T012 [P] Create tests/test_task.py with basic test structure
- [X] T013 [P] Create tests/test_todo_list.py with basic test structure
- [X] T014 [P] Create tests/test_cli.py with basic test structure

## Phase 3: [US8] Task Model and In-Memory Storage

**Goal**: Implement the Task model and basic in-memory storage functionality

**Independent Test**: Can create Task objects and verify they have the correct attributes; can instantiate TodoList and store/retrieve tasks.

**Acceptance Criteria**:
- Task objects have id, title, description, and completed attributes
- TodoList can store tasks and maintain them in memory
- New tasks get unique IDs starting from 1
- New tasks have default status of pending

- [X] T015 [US8] Implement Task dataclass with id, title, description, completed attributes in src/todo/task.py
- [X] T016 [US8] Add validation to Task to ensure title is not empty in src/todo/task.py
- [X] T017 [US8] Implement __repr__ method for Task in src/todo/task.py
- [X] T018 [US8] Implement TodoList class with internal task storage in src/todo/todo_list.py
- [X] T019 [US8] Implement ID generation mechanism in TodoList in src/todo/todo_list.py
- [X] T020 [US8] Write unit tests for Task model in tests/test_task.py
- [X] T021 [US8] Write unit tests for TodoList initialization in tests/test_todo_list.py

## Phase 4: [US1] Add a New Task

**Goal**: Allow users to add new tasks with required title and optional description

**Independent Test**: Can add a new task with a title and optional description, and verify it appears in the task list with a unique ID and pending status.

**Acceptance Criteria**:
- System allows users to provide a title (required) when adding a new task
- System allows users to provide a description (optional) when adding a new task
- System assigns each new task an auto-generated unique ID (integer, starting from 1)
- System sets the default status of new tasks to pending
- System validates that the title cannot be empty
- System provides clear error feedback when title is empty

- [X] T022 [US1] Implement TodoList.add_task() method with validation in src/todo/todo_list.py
- [X] T023 [US1] Implement ID auto-generation in add_task method in src/todo/todo_list.py
- [X] T024 [US1] Implement title validation in add_task method in src/todo/todo_list.py
- [X] T025 [US1] Add CLI method for adding tasks in src/todo/cli.py
- [X] T026 [US1] Implement user input handling for adding tasks in src/todo/cli.py
- [X] T027 [US1] Write unit tests for add_task functionality in tests/test_todo_list.py
- [X] T028 [US1] Write unit tests for add task CLI flow in tests/test_cli.py

## Phase 5: [US2] List/View All Tasks

**Goal**: Display all tasks in a clear table/format with ID, Title, Description, and Status

**Independent Test**: Can add multiple tasks and then view the list to ensure all tasks are displayed correctly with their ID, title, description, and status.

**Acceptance Criteria**:
- System displays all tasks in a clear table/format
- System shows ID, Title, Description (truncated if long), and Status for each task
- System uses [ ] indicator for pending tasks and [✓] for completed tasks
- System handles empty list gracefully with a friendly message
- System sorts tasks by ID in ascending order

- [X] T029 [US2] Implement TodoList.list_tasks() method in src/todo/todo_list.py
- [X] T030 [US2] Implement task sorting by ID in list_tasks method in src/todo/todo_list.py
- [X] T031 [US2] Add method to format tasks for display in src/todo/todo_list.py
- [X] T032 [US2] Implement CLI method for listing tasks in src/todo/cli.py
- [X] T033 [US2] Implement table formatting for task display in src/todo/cli.py
- [X] T034 [US2] Handle empty list case with friendly message in src/todo/cli.py
- [X] T035 [US2] Write unit tests for list_tasks functionality in tests/test_todo_list.py
- [X] T036 [US2] Write unit tests for list task CLI flow in tests/test_cli.py

## Phase 6: [US5] Mark Task as Complete/Incomplete

**Goal**: Allow users to toggle task status between pending and completed by ID

**Independent Test**: Can toggle the status of a task and verify the status changes correctly.

**Acceptance Criteria**:
- System allows users to mark tasks as complete/incomplete by ID
- System toggles status between pending and completed (pending ↔ completed)
- System validates that the task ID exists before toggling status
- System provides clear feedback when operations are successful
- System provides clear error messages for invalid IDs

- [X] T037 [US5] Implement TodoList.mark_task() method with ID validation in src/todo/todo_list.py
- [X] T038 [US5] Implement status toggle logic in mark_task method in src/todo/todo_list.py
- [X] T039 [US5] Add CLI method for marking tasks in src/todo/cli.py
- [X] T040 [US5] Implement user input handling for marking tasks in src/todo/cli.py
- [X] T041 [US5] Write unit tests for mark_task functionality in tests/test_todo_list.py
- [X] T042 [US5] Write unit tests for mark task CLI flow in tests/test_cli.py

## Phase 7: [US3] Update a Task

**Goal**: Allow users to update task details by ID

**Independent Test**: Can update an existing task's title and/or description and verify the changes are saved.

**Acceptance Criteria**:
- System allows users to update tasks by ID
- System allows updating title and/or description
- System validates that the task ID exists before updating
- System validates that updated title is not empty
- System provides clear error messages for validation failures
- System updates only the fields that the user specifies

- [X] T043 [US3] Implement TodoList.update_task() method with validation in src/todo/todo_list.py
- [X] T044 [US3] Implement ID validation in update_task method in src/todo/todo_list.py
- [X] T045 [US3] Implement title validation in update_task method in src/todo/todo_list.py
- [X] T046 [US3] Add CLI method for updating tasks in src/todo/cli.py
- [X] T047 [US3] Implement user input handling for updating tasks in src/todo/cli.py
- [X] T048 [US3] Implement prompting for what to update in src/todo/cli.py
- [X] T049 [US3] Write unit tests for update_task functionality in tests/test_todo_list.py
- [X] T050 [US3] Write unit tests for update task CLI flow in tests/test_cli.py

## Phase 8: [US4] Delete a Task

**Goal**: Allow users to delete tasks by ID with confirmation

**Independent Test**: Can delete an existing task and verify it no longer appears in the task list.

**Acceptance Criteria**:
- System allows users to delete tasks by ID
- System confirms deletion before removing a task
- System validates that the task ID exists before deletion
- System provides clear error messages for invalid IDs
- System permanently removes the task from the list upon confirmation

- [X] T051 [US4] Implement TodoList.delete_task() method with validation in src/todo/todo_list.py
- [X] T052 [US4] Implement ID validation in delete_task method in src/todo/todo_list.py
- [X] T053 [US4] Add CLI method for deleting tasks in src/todo/cli.py
- [X] T054 [US4] Implement user confirmation for deletion in src/todo/cli.py
- [X] T055 [US4] Implement user input handling for deleting tasks in src/todo/cli.py
- [X] T056 [US4] Write unit tests for delete_task functionality in tests/test_todo_list.py
- [X] T057 [US4] Write unit tests for delete task CLI flow in tests/test_cli.py

## Phase 9: [US6] Main CLI Loop and Menu

**Goal**: Provide a simple text-based menu interface for navigation

**Independent Test**: Can navigate through the menu options and ensure each option performs the correct action.

**Acceptance Criteria**:
- System provides a simple text-based menu with numbered options
- System includes options for Add, List, Update, Delete, Mark Complete/Incomplete, and Exit
- System handles invalid menu input gracefully without crashing
- System loops until the user chooses to exit

- [X] T058 [US6] Implement main menu display in src/todo/cli.py
- [X] T059 [US6] Implement main application loop in src/todo/cli.py
- [X] T060 [US6] Implement menu option processing in src/todo/cli.py
- [X] T061 [US6] Implement graceful handling of invalid menu input in src/todo/cli.py
- [X] T062 [US6] Integrate all task operations into CLI menu in src/todo/cli.py
- [X] T063 [US6] Implement exit functionality in src/todo/cli.py
- [X] T064 [US6] Write unit tests for CLI menu functionality in tests/test_cli.py

## Phase 10: [US7] Error Handling and Input Validation

**Goal**: Handle errors gracefully and validate all inputs

**Independent Test**: Can provide various invalid inputs and verify the app handles them gracefully with helpful error messages.

**Acceptance Criteria**:
- System validates all user inputs
- System never crashes on invalid input (wrong ID, empty title, etc.)
- System shows helpful error messages for all validation failures
- System continues normal operation after displaying error messages

- [X] T065 [US7] Implement comprehensive input validation in CLI methods in src/todo/cli.py
- [X] T066 [US7] Add error handling for invalid task IDs in all operations in src/todo/cli.py
- [X] T067 [US7] Add error handling for empty titles in all operations in src/todo/cli.py
- [X] T068 [US7] Implement graceful error handling in main loop in src/todo/cli.py
- [X] T069 [US7] Add helpful error messages throughout the application in src/todo/cli.py
- [X] T070 [US7] Write unit tests for error handling scenarios in tests/test_cli.py
- [X] T071 [US7] Write unit tests for validation scenarios in tests/test_todo_list.py

## Phase 11: Polish & Cross-Cutting Concerns

- [X] T072 Update README.md with detailed usage instructions
- [X] T073 Add example usage scenarios to README.md
- [X] T074 Implement any additional formatting improvements for task display
- [X] T075 Run full test suite and ensure all tests pass
- [X] T076 Perform manual testing of all functionality
- [X] T077 Update CLAUDE.md with implementation details
- [X] T078 Final code review and cleanup
- [ ] T079 Ensure 95%+ test coverage for core logic