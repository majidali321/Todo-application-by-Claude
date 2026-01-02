# Spec: MarkTaskComplete Reusable Skill

## Description
The MarkTaskComplete skill is a reusable method within the TodoManager class that provides functionality to toggle the completion status of a task by its unique identifier. This skill follows clean code principles with proper type hints, comprehensive documentation, and error handling for invalid task IDs.

## User Stories

### US-001: Toggle Task Completion
**As a** TodoManager user,
**I want** to mark a task as complete or incomplete by its ID,
**So that** I can track the progress of my tasks.

### US-002: Receive Updated Task
**As a** TodoManager user,
**I want** to receive the updated task dictionary after toggling completion status,
**So that** I can verify the change and display the current state.

### US-003: Error on Invalid ID
**As a** TodoManager user,
**I want** to receive a clear error when providing a non-existent task ID,
**So that** I can handle invalid input appropriately.

## Functional Requirements

### REQ-001: Method Signature
- MarkTaskComplete must be implemented as an instance method in the TodoManager class
- Method must accept task_id as a required integer parameter
- Method must return a dictionary representing the updated task

### REQ-002: Task Lookup
- Method must find the task in self.tasks by matching the id field
- Method must perform a linear search through the tasks list
- Method must locate exactly one task with the matching ID

### REQ-003: Toggle Completion Status
- Method must toggle the completed field between True and False
- If task.completed is False, set to True (mark as complete)
- If task.completed is True, set to False (mark as incomplete)
- Toggle operation must be atomic (single operation per method call)

### REQ-004: Return Updated Task
- Method must return the complete task dictionary after toggling
- Returned task must contain all fields: id, title, description, completed
- The completed field in returned task must reflect the new (toggled) state

### REQ-005: Error Handling for Invalid ID
- Method must raise ValueError if no task with the given ID is found
- Error message must be descriptive and indicate the invalid task ID
- No modifications to internal state should occur when ID is invalid

### REQ-006: Input Validation
- Method must validate that task_id is an integer type
- Method must raise TypeError if task_id is not an integer
- Method should validate that task_id is positive (optional, depends on ID assignment strategy)

### REQ-007: Clean Code Compliance
- Method must include type hints for all parameters and return value
- Method must have a docstring following Python conventions (PEP 257)
- Method must have clear, descriptive naming
- Method must not print to console (return-only design)

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| task_id | int | Yes | N/A | The unique identifier of the task to toggle. Must be an integer. |

## Output Format

The method returns a dictionary representing the updated task:

**Toggle from Incomplete to Complete:**
```json
{
  "id": 1,
  "title": "Complete project specification",
  "description": "Write detailed spec for AddTask feature",
  "completed": true
}
```

**Toggle from Complete to Incomplete:**
```json
{
  "id": 1,
  "title": "Complete project specification",
  "description": "Write detailed spec for AddTask feature",
  "completed": false
}
```

**Response Schema:**
- `id` (integer): Unique identifier for the task (unchanged)
- `title` (string): The task title (unchanged)
- `description` (string): The task description (unchanged)
- `completed` (boolean): New completion status after toggle operation

## Example Usage

### Basic Usage - Mark Task Complete
```python
from todo_manager import TodoManager

# Initialize TodoManager and add tasks
manager = TodoManager()
task = manager.add_task("Buy groceries", description="Milk, eggs, bread")
print(task)
# Output: {'id': 1, 'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'completed': False}

# Mark task as complete
updated_task = manager.mark_complete(task_id=1)
print(updated_task)
# Output: {'id': 1, 'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'completed': True}

# Verify toggle - mark as incomplete again
updated_task = manager.mark_complete(task_id=1)
print(updated_task)
# Output: {'id': 1, 'title': 'Buy groceries', 'description': 'Milk, eggs, bread', 'completed': False}
```

### Multiple Tasks
```python
manager = TodoManager()
manager.add_task("Write documentation")
manager.add_task("Run tests")
manager.add_task("Deploy application")

# Mark second task as complete
updated = manager.mark_complete(task_id=2)
print(f"Task {updated['id']} completion status: {updated['completed']}")
# Output: Task 2 completion status: True

# View all tasks
all_tasks = manager.view_tasks()
for task in all_tasks:
    status = "✓" if task['completed'] else "○"
    print(f"{status} [{task['id']}] {task['title']}")
# Output:
# ○ [1] Write documentation
# ✓ [2] Run tests
# ○ [3] Deploy application
```

### Error Handling - Invalid Task ID
```python
manager = TodoManager()
manager.add_task("Sample task")

try:
    # Invalid: task doesn't exist
    manager.mark_complete(task_id=999)
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Task with ID 999 not found
```

### Error Handling - Invalid Type
```python
manager = TodoManager()
manager.add_task("Sample task")

try:
    # Invalid: task_id is not an integer
    manager.mark_complete(task_id="not-an-int")
except TypeError as e:
    print(f"Error: {e}")
    # Output: Error: Task ID must be an integer

try:
    # Invalid: task_id is None
    manager.mark_complete(task_id=None)
except TypeError as e:
    print(f"Error: {e}")
    # Output: Error: Task ID must be an integer
```

### Using Return Value for Verification
```python
manager = TodoManager()
manager.add_task("Complete project")

# Toggle and verify
result = manager.mark_complete(task_id=1)
if result['completed']:
    print("Task marked as complete!")
else:
    print("Task marked as incomplete!")
# Output: Task marked as complete!

# Toggle again
result = manager.mark_complete(task_id=1)
if result['completed']:
    print("Task marked as complete!")
else:
    print("Task marked as incomplete!")
# Output: Task marked as incomplete!
```

## Edge Cases

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| Invalid task ID | Provided ID does not exist in tasks list | Raise ValueError with message "Task with ID {task_id} not found" |
| Non-integer task_id | task_id is string, float, None, or other type | Raise TypeError with message "Task ID must be an integer" |
| Negative task ID | task_id is a negative integer | Treat as invalid (no such ID), raise ValueError |
| Zero task ID | task_id is 0 | Treat as invalid (no such ID), raise ValueError |
| Empty task list | No tasks exist in manager | Raise ValueError for any task_id provided |
| Task already completed | Task.completed is already True | Toggle to False (mark as incomplete) |
| Task already incomplete | Task.completed is already False | Toggle to True (mark as complete) |
| Multiple identical IDs | Two tasks with same ID (should not happen) | Return first match; document that IDs must be unique |
| Task with None fields | Task dict contains None values for some fields | Toggle completed field regardless; return task as-is otherwise |
| Concurrent modifications | Tasks list modified during operation | Toggle on current snapshot; document as not thread-safe |

## References to Constitution.md

### Principle: Reusable Intelligence
- [CONSTITUTION: PRINCIPLE-REUSABLE-CODE] This skill demonstrates commitment to creating reusable, modular components that can be leveraged across the application
- The mark_complete method is designed as a self-contained unit with clear inputs/outputs, independent of external dependencies
- Encapsulates task completion logic for easy reuse in various contexts (CLI, API, tests)

### Principle: Clean Code Standards
- [CONSTITUTION: PRINCIPLE-CLEAN-CODE] Adherence to type hints, docstrings, and single responsibility principle
- Method has one clear purpose: toggle task completion status
- Clear, descriptive naming following Python conventions
- No side-channel outputs (no printing), return-only design

### Principle: Defensive Programming
- [CONSTITUTION: PRINCIPLE-DEFENSIVE-PROGRAMMING] Comprehensive input validation and error handling
- Validates task_id type before processing
- Raises appropriate exceptions (ValueError, TypeError) with descriptive messages
- No state modifications when input is invalid

### Principle: Testability
- [CONSTITUTION: PRINCIPLE-TEST-FIRST] Pure function design (aside from internal state modification) enables straightforward unit testing
- Input/output contract is explicit and verifiable
- Error conditions are clearly defined and testable
- Toggle operation is deterministic and easy to verify

## Acceptance Criteria

### AC-001: Toggle Incomplete to Complete
**Given** a TodoManager instance with a task where completed=False
**When** I call mark_complete(task_id=<task-id>)
**Then** the task's completed field is toggled to True
**And** the returned task dictionary has completed=True

### AC-002: Toggle Complete to Incomplete
**Given** a TodoManager instance with a task where completed=True
**When** I call mark_complete(task_id=<task-id>)
**Then** the task's completed field is toggled to False
**And** the returned task dictionary has completed=False

### AC-003: Return Updated Task
**Given** a TodoManager instance with a task
**When** I call mark_complete(task_id=<task-id>)
**Then** a complete task dictionary is returned
**And** it contains all fields: id, title, description, completed
**And** all field values match the task's current state (except toggled completed)

### AC-004: Error on Invalid Task ID
**Given** a TodoManager instance with tasks having IDs [1, 2, 3]
**When** I call mark_complete(task_id=999)
**Then** a ValueError is raised
**And** the error message indicates the task was not found
**And** no task is modified in self.tasks

### AC-005: Error on Non-Integer ID
**Given** a TodoManager instance with tasks
**When** I call mark_complete(task_id="not-an-int")
**Then** a TypeError is raised
**And** the error message indicates task_id must be an integer
**And** no task is modified in self.tasks

### AC-006: Task ID Validation - Negative
**Given** a TodoManager instance with tasks
**When** I call mark_complete(task_id=-1)
**Then** a ValueError is raised
**And** no task is modified in self.tasks

### AC-007: Preserve Other Task Fields
**Given** a TodoManager instance with a task having title="Test", description="Testing"
**When** I call mark_complete(task_id=<task-id>)
**Then** the returned task has title="Test" (unchanged)
**And** the returned task has description="Testing" (unchanged)
**And** only the completed field has changed

### AC-008: Type Hints Present
**Given** the MarkTaskComplete method implementation
**When** I inspect the method signature
**Then** type hints are present for:
- task_id: int
- Return type: Dict[str, Any]

### AC-009: Docstring Present
**Given** the MarkTaskComplete method implementation
**When** I inspect the method docstring
**Then** it includes:
- Brief description of what the method does
- Documentation for all parameters
- Documentation for return value
- Description of possible exceptions (ValueError, TypeError)

### AC-010: No Console Output
**Given** a TodoManager instance with a task
**When** I call mark_complete(task_id=<task-id>)
**Then** nothing is printed to the console
**And** all output is via return value only

### AC-011: Multiple Toggle Operations
**Given** a TodoManager instance with a task where completed=False
**When** I call mark_complete(task_id=<task-id>) twice
**Then** after the first call, completed=True
**And** after the second call, completed=False
**And** the final state equals the initial state

### AC-012: Find Task by Correct ID
**Given** a TodoManager instance with tasks: [id=1, id=2, id=3]
**When** I call mark_complete(task_id=2)
**Then** only the task with id=2 is modified
**And** tasks with id=1 and id=3 remain unchanged

## Non-Functional Requirements

### Performance
- Task lookup and toggle operation must complete in O(n) time complexity (linear search through tasks list)
- Method should not perform unnecessary operations beyond the toggle
- For small to medium task lists (<1000 tasks), operation should complete in <10ms

### Maintainability
- Code must be self-documenting with clear variable names
- Method must be easily understandable without external documentation
- Toggle logic should be obvious and not overly complex

### Scalability Considerations
- Linear search is acceptable for current scope (in-memory task list)
- Document performance considerations for very large task lists (>10,000 tasks)
- Note that if performance becomes an issue, consider using a dictionary for O(1) task lookup

### Data Integrity
- Toggle operation must be atomic (no intermediate inconsistent state)
- If an error occurs, no partial modifications should be made to internal state
- Method should not corrupt or lose task data

## Implementation Notes

### Class Structure
```python
from typing import Dict, Any

class TodoManager:
    """Manages a collection of todo tasks."""

    def __init__(self):
        """Initialize an empty task list and ID counter."""
        self.tasks: List[Dict[str, Any]] = []
        self._next_id: int = 1

    def mark_complete(self, task_id: int) -> Dict[str, Any]:
        """
        Toggle the completion status of a task by its ID.

        This method finds a task by its unique identifier and toggles its
        completed status between True and False. If the task is incomplete
        (completed=False), it will be marked as complete. If it is already
        complete (completed=True), it will be marked as incomplete.

        Args:
            task_id: The unique identifier of the task to toggle.
                    Must be an integer corresponding to an existing task.

        Returns:
            A dictionary representing the updated task with keys:
            - id: Unique integer identifier (unchanged)
            - title: Task title string (unchanged)
            - description: Task description string (unchanged)
            - completed: Boolean completion status (toggled)

        Raises:
            ValueError: If no task with the given task_id exists.
            TypeError: If task_id is not an integer type.
        """
        # Implementation to be completed
        pass
```

### Key Implementation Details
1. Validate that task_id is an integer type (raise TypeError if not)
2. Iterate through self.tasks to find the task with matching id
3. If task is found, toggle the completed field using: `task['completed'] = not task['completed']`
4. Return the complete task dictionary after toggle
5. If task is not found after full iteration, raise ValueError
6. Use descriptive error messages that include the invalid task_id

### Implementation Example
```python
def mark_complete(self, task_id: int) -> Dict[str, Any]:
    # Validate input type
    if not isinstance(task_id, int):
        raise TypeError(f"Task ID must be an integer, got {type(task_id).__name__}")

    # Find task by ID
    for task in self.tasks:
        if task['id'] == task_id:
            # Toggle completion status
            task['completed'] = not task['completed']
            return task

    # Task not found
    raise ValueError(f"Task with ID {task_id} not found")
```

### Alternative Implementation Approaches

**Option 1: Linear Search (Current Recommendation)**
```python
def mark_complete(self, task_id: int) -> Dict[str, Any]:
    for task in self.tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            return task
    raise ValueError(f"Task with ID {task_id} not found")
```
- Pros: Simple, no additional data structures, works with current list-based storage
- Cons: O(n) time complexity, slower for very large lists

**Option 2: Dictionary Lookup (If Refactored)**
```python
def mark_complete(self, task_id: int) -> Dict[str, Any]:
    if task_id not in self.tasks_by_id:  # Would need tasks_by_id dict
        raise ValueError(f"Task with ID {task_id} not found")
    task = self.tasks_by_id[task_id]
    task['completed'] = not task['completed']
    return task
```
- Pros: O(1) time complexity, faster for large datasets
- Cons: Requires refactoring storage to maintain dictionary in addition to list

**Recommended**: Use linear search (Option 1) for current scope, document performance considerations for future optimization

## Related Features
- AddTask: Create and add new tasks
- ViewTaskList: Get all tasks
- GetTaskById: Retrieve a single task by ID (future enhancement)
- DeleteTask: Remove a task from the list (future enhancement)
- UpdateTask: Modify task details (future enhancement)

## Test Strategy

### Unit Test Cases
1. Test toggle from incomplete to complete
2. Test toggle from complete to incomplete
3. Test multiple toggle operations return to original state
4. Test ValueError for non-existent task ID
5. Test TypeError for non-integer task_id
6. Test TypeError for None task_id
7. Test ValueError for negative task_id
8. Test ValueError for zero task_id
9. Test returned task contains all required fields
10. Test other task fields remain unchanged after toggle
11. Test correct task is modified when multiple tasks exist
12. Test type hints are present in method signature
13. Test docstring is present and complete
14. Test no console output during operation

### Integration Test Cases
1. Test mark_complete() after adding tasks via add_task()
2. Test view_tasks() reflects updated completion status after mark_complete()
3. Test multiple mark_complete() calls on the same task
4. Test mark_complete() works with tasks that have descriptions
5. Test mark_complete() works with tasks that have empty descriptions
6. Test mark_complete() maintains task order in the list

### Edge Case Test Cases
1. Test behavior with very large task_id numbers
2. Test behavior when task_id is a very large positive integer
3. Test behavior with Unicode characters in task title/description
4. Test behavior with special characters in task fields
5. Test concurrent access (if threading is later added)

## Change History
| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-01-02 | Spec-Writer | Initial specification for MarkTaskComplete skill |

---

**Status**: Ready for Implementation
**Approver**: TBD
**Implementation Start**: TBD
**Estimated Complexity**: Low
