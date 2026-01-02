# Feature: UpdateTask Skill

## Description
The UpdateTask skill is a reusable method within the TodoManager class that provides functionality to modify existing tasks in an in-memory task list. This skill follows clean code principles with proper type hints, comprehensive documentation, and defensive programming practices. It supports partial updates, allowing users to modify only specific fields while preserving the rest of the task data.

## User Stories

### US-001: Update Task Title
**As a** TodoManager user,
**I want** to update the title of an existing task,
**So that** I can correct mistakes or refine task descriptions.

### US-002: Update Task Description
**As a** TodoManager user,
**I want** to update the description of an existing task,
**So that** I can add more details or clarify task requirements.

### US-003: Partial Field Updates
**As a** TodoManager user,
**I want** to update only the fields I specify without affecting other fields,
**So that** I can make incremental changes to tasks safely.

## Functional Requirements

### REQ-001: Method Signature
- UpdateTask must be implemented as an instance method in the TodoManager class
- Method must accept task_id as a required integer parameter
- Method must accept title as an optional string parameter with default value None
- Method must accept description as an optional string parameter with default value None

### REQ-002: Task Lookup
- Method must find the task by task_id in self.tasks list
- Task ID matching must be exact (integer equality)
- Method must raise ValueError if task_id does not exist

### REQ-003: Partial Update Logic
- Method must update only non-None parameters (title and/or description)
- If title is None, the existing title must remain unchanged
- If description is None, the existing description must remain unchanged
- The 'id' field must never be modified
- The 'completed' field must never be modified

### REQ-004: Update Validation
- Method must raise ValueError if both title and description are None (no updates provided)
- If title is provided (not None), it must be a non-empty string after whitespace stripping
- If title fails validation, ValueError must be raised and no updates should occur
- If description is provided (not None), it can be any string (including empty string)

### REQ-005: Return Value
- Method must return the complete updated task dictionary
- Return value must include all fields (id, title, description, completed) with current values
- The returned dictionary should reflect all applied changes

### REQ-006: In-Memory Modification
- Updates must be applied directly to the task dictionary in self.tasks list
- No copy of the task should be created; the original task dict should be modified
- Changes must be immediately visible to other methods accessing the task

### REQ-007: Clean Code Compliance
- Method must include type hints for all parameters and return value
- Method must have a docstring following Python conventions (PEP 257)
- Method must validate inputs before modifying state
- Method must maintain transactional integrity: either all updates succeed or none do

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| task_id | int | Yes | N/A | The unique identifier of the task to update. Must exist in the task list. |
| title | str \| None | No | None | New title for the task. If None, existing title is preserved. Must be non-empty if provided. |
| description | str \| None | No | None | New description for the task. If None, existing description is preserved. Can be empty string if provided. |

## Output Format

The method returns a dictionary representing the updated task:

```json
{
  "id": 2,
  "title": "Updated task title",
  "description": "Updated task description",
  "completed": false
}
```

**Response Schema:**
- `id` (integer): The unique identifier (unchanged from original task)
- `title` (string): The task title (either updated or original value)
- `description` (string): The task description (either updated or original value)
- `completed` (boolean): Task completion status (unchanged from original task)

## Example Usage

### Update Title Only
```python
from todo_manager import TodoManager

# Initialize TodoManager and add a task
manager = TodoManager()
task = manager.add_task("Buy groceries", "Milk, eggs, bread")
# Task: {'id': 1, 'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'completed': False}

# Update title only
updated = manager.update_task(task_id=1, title="Buy weekly groceries")
print(updated)
# Output: {'id': 1, 'title': 'Buy weekly groceries', 'description': 'Milk, eggs, bread', 'completed': False}
```

### Update Description Only
```python
# Update description only
updated = manager.update_task(task_id=1, description="Milk, eggs, bread, and butter")
print(updated)
# Output: {'id': 1, 'title': 'Buy weekly groceries', 'description': 'Milk, eggs, bread, and butter', 'completed': False}
```

### Update Both Fields
```python
# Update both title and description
updated = manager.update_task(
    task_id=1,
    title="Buy groceries for the week",
    description="Weekly grocery shopping: milk, eggs, bread, butter, fruits"
)
print(updated)
# Output: {'id': 1, 'title': 'Buy groceries for the week', 'description': 'Weekly grocery shopping: milk, eggs, bread, butter, fruits', 'completed': False}
```

### Set Empty Description
```python
# Clear the description by setting it to empty string
updated = manager.update_task(task_id=1, description="")
print(updated)
# Output: {'id': 1, 'title': 'Buy groceries for the week', 'description': '', 'completed': False}
```

### Error Handling Examples
```python
manager = TodoManager()

# Task not found error
try:
    manager.update_task(task_id=999, title="New title")
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Task with ID 999 not found

# No updates provided error
try:
    manager.update_task(task_id=1)
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: At least one field (title or description) must be provided for update

# Empty title error
try:
    manager.update_task(task_id=1, title="")
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Task title cannot be empty

# None title is not an error (it means "don't update title")
# This is valid - will only update description
updated = manager.update_task(task_id=1, description="New description")
# Works fine, title remains unchanged
```

## Edge Cases

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| Task ID not found | task_id does not match any existing task | Raise ValueError with message "Task with ID {task_id} not found" |
| Both parameters None | Neither title nor description is provided | Raise ValueError with message "At least one field (title or description) must be provided for update" |
| Empty title string | User provides "" as title | Raise ValueError with message "Task title cannot be empty" |
| Whitespace-only title | User provides "   " as title | Strip whitespace; if empty after stripping, raise ValueError |
| Empty description | User provides "" as description | Accept empty string as valid update (clears the description) |
| Non-existent task | task_id is negative, zero, or out of range | Same as "Task ID not found" - raise ValueError |
| Task with completed=True | User updates a completed task | Allow update; completed status remains unchanged |
| Title equals current value | User sets title to same value | Allow update; no data change but returns successfully |
| Very long title/description | Strings exceed reasonable length | Allow storage but document as potential UI concern |
| Unicode characters | Fields contain non-ASCII characters | Support full Unicode; no special handling needed |
| Special characters | Fields contain quotes, newlines, etc. | Accept as-is; Python dictionaries handle serialization |
| Concurrent updates | Multiple operations on same task | Document as thread-unsafe for current scope |

## References to Constitution.md

### Principle: Reusable Intelligence
- [CONSTITUTION: PRINCIPLE-REUSABLE-CODE] This skill demonstrates commitment to creating reusable, modular components that can be leveraged across the application
- The UpdateTask method is designed as a self-contained unit with clear inputs/outputs, independent of external dependencies
- Encapsulates task update logic for easy reuse in various contexts (CLI, API, tests)
- Partial update pattern promotes flexibility in task management workflows

### Principle: Clean Code Standards
- [CONSTITUTION: PRINCIPLE-CLEAN-CODE] Adherence to type hints, docstrings, and single responsibility principle
- Method has one clear purpose: modify an existing task
- Input validation occurs before any state modification
- Clear, descriptive naming following Python conventions
- Transactional update approach ensures data consistency

### Principle: Defensive Programming
- [CONSTITUTION: PRINCIPLE-DEFENSIVE-PROGRAMMING] Robust error handling and input validation
- Validates all inputs before modifying state
- Validates task existence before attempting updates
- Ensures at least one field is being updated to prevent no-op calls
- Protects critical fields (id, completed) from modification

### Principle: Testability
- [CONSTITUTION: PRINCIPLE-TEST-FIRST] Pure function design enables straightforward unit testing
- Input/output contract is explicit and verifiable
- Error conditions are clearly defined and testable
- Partial update behavior is easily testable through various parameter combinations

## Acceptance Criteria

### AC-001: Update Title Only
**Given** a TodoManager with an existing task with id=1, title="Old title", description="Old description"
**When** I call update_task(task_id=1, title="New title")
**Then** the returned task has title="New title"
**And** the description remains "Old description"
**And** the id and completed fields remain unchanged

### AC-002: Update Description Only
**Given** a TodoManager with an existing task
**When** I call update_task(task_id=1, description="New description")
**Then** the returned task has description="New description"
**And** the title remains unchanged
**And** the id and completed fields remain unchanged

### AC-003: Update Both Fields
**Given** a TodoManager with an existing task
**When** I call update_task(task_id=1, title="New title", description="New description")
**Then** the returned task has both updated values
**And** the id and completed fields remain unchanged

### AC-004: Clear Description
**Given** a TodoManager with a task that has a non-empty description
**When** I call update_task(task_id=1, description="")
**Then** the returned task has description=""
**And** all other fields remain unchanged

### AC-005: Task Not Found Error
**Given** a TodoManager with existing tasks (ids 1, 2, 3)
**When** I call update_task(task_id=999, title="Test")
**Then** a ValueError is raised
**And** the error message indicates task not found
**And** no task is modified

### AC-006: No Updates Provided Error
**Given** a TodoManager with an existing task
**When** I call update_task(task_id=1) without title or description
**Then** a ValueError is raised
**And** the error message indicates at least one field must be provided
**And** no task is modified

### AC-007: Empty Title Validation
**Given** a TodoManager with an existing task
**When** I call update_task(task_id=1, title="")
**Then** a ValueError is raised
**And** the error message indicates title cannot be empty
**And** the task remains unchanged

### AC-008: Whitespace Title Validation
**Given** a TodoManager with an existing task
**When** I call update_task(task_id=1, title="   ")
**Then** a ValueError is raised
**And** the error message indicates title cannot be empty
**And** the task remains unchanged

### AC-009: ID Field Immutable
**Given** a TodoManager with a task with id=1
**When** I call update_task on this task
**Then** the id field remains 1 in the returned task
**And** the task's id in self.tasks is unchanged

### AC-010: Completed Field Immutable
**Given** a TodoManager with a task with completed=False
**When** I call update_task on this task
**Then** the completed field remains False in the returned task
**And** the task's completed status in self.tasks is unchanged

### AC-011: In-Memory Modification
**Given** a TodoManager with an existing task
**When** I call update_task and retrieve the task again from self.tasks
**Then** the same dictionary object reflects the updates (not a copy)

### AC-012: Type Hints Present
**Given** the UpdateTask method implementation
**When** I inspect the method signature
**Then** type hints are present for:
- task_id: int
- title: Optional[str]
- description: Optional[str]
- Return type: Dict[str, Any]

### AC-013: Docstring Present
**Given** the UpdateTask method implementation
**When** I inspect the method docstring
**Then** it includes:
- Brief description of what the method does
- Documentation for all parameters
- Documentation for return value
- Description of possible exceptions

### AC-014: Update Completed Task
**Given** a TodoManager with a task with completed=True
**When** I call update_task on this task
**Then** the update succeeds
**And** the completed field remains True
**And** the title and/or description are updated as requested

### AC-015: Same Title Update
**Given** a TodoManager with a task with title="Test"
**When** I call update_task(task_id=1, title="Test")
**Then** the call succeeds without error
**And** the task remains unchanged (idempotent update)

## Non-Functional Requirements

### Performance
- Task lookup operation should complete in O(n) time complexity (linear search)
- Update operation should complete in O(1) time complexity once task is found
- Method should not perform unnecessary operations beyond validation and field updates

### Maintainability
- Code must be self-documenting with clear variable names
- Method must be easily understandable without external documentation
- Changes to the method should not break backward compatibility without versioning
- Partial update pattern should be clearly documented in code comments

### Data Integrity
- Updates must be atomic: either all updates succeed or none do
- No partial application of updates should occur
- Validation failures must not modify the task state
- Critical fields (id, completed) must remain immutable

### Scalability Considerations
- In-memory storage is suitable for current scope
- Linear search becomes expensive with large task lists (O(n) lookup)
- Consider optimizing with a dictionary index if task list grows large
- Note that updates are not persistent across application restarts

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

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update an existing task in the todo list.

        Only fields that are not None will be updated. This allows partial updates
        where some fields remain unchanged. The 'id' and 'completed' fields cannot
        be modified through this method.

        Args:
            task_id: The unique identifier of the task to update (required).
            title: New title for the task (optional). If None, existing title is preserved.
                  Must be non-empty if provided.
            description: New description for the task (optional). If None, existing
                        description is preserved. Can be empty string if provided.

        Returns:
            A dictionary representing the updated task with all fields:
            - id: Unique integer identifier (unchanged)
            - title: Updated task title string
            - description: Updated task description string
            - completed: Boolean completion status (unchanged)

        Raises:
            ValueError: If task_id is not found, no updates provided, or title is empty.
        """
        # Implementation to be completed
        pass
```

### Key Implementation Details
1. Iterate through `self.tasks` to find task with matching `id`
2. Raise ValueError if task not found
3. Validate that at least one of title or description is not None
4. If title is provided, validate it's a non-empty string (strip whitespace)
5. Update fields in-place: modify the existing task dictionary directly
6. Do not modify 'id' or 'completed' fields
7. Return the complete task dictionary after updates
8. Perform all validation before any state modification

### Validation Order
1. Find task by ID (raises if not found)
2. Check at least one update field provided (raises if both None)
3. If title provided, validate it's non-empty (raises if empty)
4. Only after all validations pass, apply updates

### Transactional Update Approach
- Store original field values before update (for rollback if needed, though not strictly necessary with input validation)
- Or simply validate all inputs first, then apply updates in sequence
- Either approach ensures no partial updates occur on validation failure

## Related Features
- AddTask: Create new tasks
- ViewTask: Retrieve a task by ID
- ListTasks: Get all tasks
- MarkTaskComplete: Mark a task as completed
- DeleteTask: Remove a task from the list

## Change History
| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-01-02 | Spec-Writer | Initial specification for UpdateTask skill |

---

**Status**: Ready for Implementation
**Approver**: TBD
**Implementation Start**: TBD
**Estimated Complexity**: Low
