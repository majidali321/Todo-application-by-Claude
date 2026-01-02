# Feature: AddTask Skill

## Description
The AddTask skill is a reusable method within the TodoManager class that provides functionality to create and store new tasks in an in-memory task list. This skill follows clean code principles with proper type hints, comprehensive documentation, and defensive programming practices.

## User Stories

### US-001: Add New Task
**As a** TodoManager user,
**I want** to add a new task with a title and optional description,
**So that** I can build and track a collection of tasks.

### US-002: Auto-Generate Task ID
**As a** TodoManager user,
**I want** each task to have a unique, incrementally assigned integer ID,
**So that** tasks can be uniquely identified and referenced.

## Functional Requirements

### REQ-001: Method Signature
- AddTask must be implemented as an instance method in the TodoManager class
- Method must accept title as a required string parameter
- Method must accept description as an optional string parameter with default value ""

### REQ-002: Unique ID Generation
- Task IDs must be unique integers
- IDs must be incrementally assigned (1, 2, 3, ...)
- ID assignment must be thread-safe for the current application scope

### REQ-003: Task Data Structure
- Task must be represented as a Python dictionary with keys: id, title, description, completed
- id: integer, auto-generated unique identifier
- title: string, provided by user
- description: string, optional, default empty string
- completed: boolean, default False

### REQ-004: Task Storage
- Task must be added to self.tasks list in TodoManager instance
- Task must be appended to the end of the list
- No persistence mechanism required (in-memory only)

### REQ-005: Return Value
- Method must return the complete newly created task dictionary
- Return value must include all fields (id, title, description, completed)

### REQ-006: Error Handling
- Method must validate that title is not empty or None
- Method must raise ValueError with descriptive message if validation fails
- Method must raise TypeError if title is not a string type

### REQ-007: Clean Code Compliance
- Method must include type hints for all parameters and return value
- Method must have a docstring following Python conventions (PEP 257)
- Method must have no side effects beyond adding task to memory
- Method must be pure in the sense that it doesn't modify external state beyond self.tasks

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| title | str | Yes | N/A | The title/name of the task. Must be non-empty. |
| description | str | No | "" | Additional details about the task. Optional field. |

## Output Format

The method returns a dictionary representing the newly created task:

```json
{
  "id": 1,
  "title": "Complete project specification",
  "description": "Write detailed spec for AddTask feature",
  "completed": false
}
```

**Response Schema:**
- `id` (integer): Auto-generated unique identifier for the task
- `title` (string): The task title as provided by the user
- `description` (string): The task description (empty string if not provided)
- `completed` (boolean): Task completion status (always False for new tasks)

## Example Usage

### Basic Usage
```python
from todo_manager import TodoManager

# Initialize TodoManager
manager = TodoManager()

# Add a task with title only
task = manager.add_task("Buy groceries")
print(task)
# Output: {'id': 1, 'title': 'Buy groceries', 'description': '', 'completed': False}

# Add a task with title and description
task = manager.add_task(
    title="Complete documentation",
    description="Write API documentation for all endpoints"
)
print(task)
# Output: {'id': 2, 'title': 'Complete documentation', 'description': 'Write API documentation for all endpoints', 'completed': False}
```

### Error Handling Example
```python
manager = TodoManager()

try:
    # Invalid: empty title
    manager.add_task("")
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Task title cannot be empty

try:
    # Invalid: None title
    manager.add_task(None)
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
    # Output: Error: Task title must be a string
```

## Edge Cases

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| Empty title string | User provides "" as title | Raise ValueError with message "Task title cannot be empty" |
| None value for title | User provides None as title | Raise TypeError with message "Task title must be a string" |
| Non-string title | User provides int, list, or other type | Raise TypeError with message "Task title must be a string" |
| Whitespace-only title | User provides "   " as title | Strip whitespace; if empty after stripping, raise ValueError |
| Very long title | Title exceeds reasonable length (e.g., 500 chars) | Allow storage but document as potential UI concern |
| Unicode characters | Title contains non-ASCII characters | Support full Unicode; no special handling needed |
| Special characters | Title contains quotes, newlines, etc. | Accept as-is; Python dictionaries handle serialization |
| Concurrent additions | Multiple threads/tasks adding simultaneously | Document as thread-unsafe for current scope; add threading note if needed |

## References to Constitution.md

### Principle: Reusable Intelligence
- [CONSTITUTION: PRINCIPLE-REUSABLE-CODE] This skill demonstrates commitment to creating reusable, modular components that can be leveraged across the application
- The AddTask method is designed as a self-contained unit with clear inputs/outputs, independent of external dependencies
- Encapsulates task creation logic for easy reuse in various contexts (CLI, API, tests)

### Principle: Clean Code Standards
- [CONSTITUTION: PRINCIPLE-CLEAN-CODE] Adherence to type hints, docstrings, and single responsibility principle
- Method has one clear purpose: create and store a task
- No side effects beyond memory modification
- Clear, descriptive naming following Python conventions

### Principle: Testability
- [CONSTITUTION: PRINCIPLE-TEST-FIRST] Pure function design enables straightforward unit testing
- Input/output contract is explicit and verifiable
- Error conditions are clearly defined and testable

## Acceptance Criteria

### AC-001: Basic Task Addition
**Given** a TodoManager instance
**When** I call add_task with title "Complete assignment"
**Then** a task dictionary is returned with:
- id = 1 (first task)
- title = "Complete assignment"
- description = ""
- completed = False

### AC-002: Task With Description
**Given** a TodoManager instance
**When** I call add_task with title="Write tests" and description="Add unit tests for add_task"
**Then** a task dictionary is returned with the provided title and description

### AC-003: Sequential IDs
**Given** a TodoManager with 2 existing tasks
**When** I call add_task to add a third task
**Then** the new task has id = 3

### AC-004: Task Storage
**Given** a TodoManager instance
**When** I add a task using add_task
**Then** the task is present in the manager.tasks list
**And** it is the last element in the list

### AC-005: Empty Title Validation
**Given** a TodoManager instance
**When** I call add_task with title=""
**Then** a ValueError is raised
**And** the error message indicates the title cannot be empty
**And** no task is added to self.tasks

### AC-006: Type Validation
**Given** a TodoManager instance
**When** I call add_task with title=None
**Then** a TypeError is raised
**And** the error message indicates title must be a string
**And** no task is added to self.tasks

### AC-007: Type Hints Present
**Given** the AddTask method implementation
**When** I inspect the method signature
**Then** type hints are present for:
- title: str
- description: str
- Return type: Dict[str, Any]

### AC-008: Docstring Present
**Given** the AddTask method implementation
**When** I inspect the method docstring
**Then** it includes:
- Brief description of what the method does
- Documentation for all parameters
- Documentation for return value
- Description of possible exceptions

### AC-009: Whitespace Title Handling
**Given** a TodoManager instance
**When** I call add_task with title="   " (only whitespace)
**Then** a ValueError is raised
**And** the error message indicates the title cannot be empty

### AC-010: No External Side Effects
**Given** a TodoManager instance
**When** I call add_task with valid parameters
**Then** no external resources (files, database, network) are accessed
**And** no external state is modified beyond self.tasks

## Non-Functional Requirements

### Performance
- Task addition operation must complete in O(1) time complexity (list append operation)
- Method should not perform unnecessary operations or validations beyond required checks

### Maintainability
- Code must be self-documenting with clear variable names
- Method must be easily understandable without external documentation
- Changes to the method should not break backward compatibility without versioning

### Scalability Considerations
- In-memory storage is suitable for current scope
- Document limitations if tasks list grows very large (memory considerations)
- Note that task IDs are not persistent across application restarts

## Implementation Notes

### Class Structure
```python
from typing import Dict, Any, Optional

class TodoManager:
    """Manages a collection of todo tasks."""

    def __init__(self):
        """Initialize an empty task list and ID counter."""
        self.tasks: list[Dict[str, Any]] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Dict[str, Any]:
        """
        Add a new task to the todo list.

        Args:
            title: The title/name of the task (required, must be non-empty).
            description: Additional details about the task (optional, defaults to "").

        Returns:
            A dictionary representing the newly created task with keys:
            - id: Unique integer identifier
            - title: Task title string
            - description: Task description string
            - completed: Boolean completion status (False for new tasks)

        Raises:
            ValueError: If title is empty or contains only whitespace.
            TypeError: If title is not a string type.
        """
        # Implementation to be completed
        pass
```

### Key Implementation Details
1. Use `self._next_id` as a private counter for generating incremental IDs
2. Increment `_next_id` after assigning to new task
3. Strip whitespace from title before validation
4. Validate title before any mutation of state
5. Create task dictionary and append to `self.tasks`
6. Return the complete task dictionary

## Related Features
- ViewTask: Retrieve a task by ID
- ListTasks: Get all tasks
- CompleteTask: Mark a task as completed
- DeleteTask: Remove a task from the list

## Change History
| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-01-02 | Spec-Writer | Initial specification for AddTask skill |

---

**Status**: Ready for Implementation
**Approver**: TBD
**Implementation Start**: TBD
**Estimated Complexity**: Low
