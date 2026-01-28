# Data Model: CLI Todo Application

**Created**: 2026-01-20
**Feature**: CLI Todo Application
**Associated Plan**: [plan.md](./plan.md)

## Task Entity

The core entity in the CLI Todo application is the Task object.

### Task Structure
```python
{
    "id": int,           # Unique identifier for the task (automatically assigned)
    "description": str   # Text description of the task
}
```

### Properties

- **id** (integer)
  - Purpose: Unique identifier for each task
  - Generation: Automatically assigned incrementally starting from 1
  - Constraints: Must be unique within the current session

- **description** (string)
  - Purpose: Human-readable description of the task
  - Constraints: Cannot be empty or consist only of whitespace
  - Validation: Trimmed of leading/trailing whitespace

## Internal Storage Model

Tasks are stored internally in a Python list structure:
```python
_tasks = [
    {"id": 1, "description": "First task"},
    {"id": 2, "description": "Second task"},
    ...
]
```

## Relationships

In this initial implementation, there are no relationships between tasks. Each task is independent.

## Data Lifecycle

- **Creation**: When a new task is added, it's assigned the next available ID and stored in the internal list
- **Reading**: Tasks can be retrieved individually by ID or all at once
- **Updating**: Not supported in this initial implementation (future enhancement)
- **Deletion**: Tasks are removed from the internal list by ID
- **Persistence**: Tasks exist only in memory during the application session (volatile storage)

## Validation Rules

1. Task descriptions cannot be empty (after trimming whitespace)
2. Task IDs must be positive integers
3. Each task must have a unique ID within the session
4. Operations on non-existent task IDs must return appropriate errors