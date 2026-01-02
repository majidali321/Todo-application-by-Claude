# Feature: DeleteTask Skill

## Description
The DeleteTask skill is a reusable method within the TodoManager class that provides functionality to permanently remove tasks from an in-memory task list. This skill follows clean code principles with proper type hints, comprehensive documentation, and defensive programming practices. It allows users to clean up their task list by removing tasks that are no longer needed.

## User Stories

### US-001: Delete Task
**As a** TodoManager user,
**I want** to delete a task by its ID,
**So that** I can remove completed or unwanted tasks from my list.

### US-002: Confirmation of Deletion
**As a** TodoManager user,
**I want** to receive confirmation when a task is successfully deleted,
**So that** I can verify the deletion operation completed.

### US-003: Handle Non-Existent Task
**As a** TodoManager user,
**I want** to receive clear feedback when attempting to delete a non-existent task,
**So that** I can understand why the operation failed.

## Functional Requirements

### REQ-001: Method Signature
- DeleteTask must be implemented as an instance method in the TodoManager class
- Method must accept task_id as a required integer parameter
- Method must return a boolean indicating success (True) or failure (False)

### REQ-002: Task Removal
- Method must remove the task with matching task_id from self.tasks list
- Removal must be permanent (no undo or restore mechanism)
- After deletion, the task should no longer be accessible through any method

### REQ-003: Task Lookup
- Method must find the task by task_id in self.tasks list
- Task ID matching must be exact (integer equality)

### REQ-004: Return Value Behavior
- Method must return True if a task was successfully found and deleted
- Method must return False if no task with the given task_id exists
- Method must not raise exceptions for non-existent tasks (graceful failure)

### REQ-005: In-Memory Modification
- Deletion must modify the self.tasks list directly
- The task object should be removed from the list, leaving a gap in indices
- Task IDs of remaining tasks must remain unchanged (IDs are not reassigned)

### REQ-006: No Side Effects
- Method must not print any output to stdout/stderr
- Method must not modify any external state beyond self.tasks
- Method must not affect the _next_id counter

### REQ-007: Clean Code Compliance
- Method must include type hints for all parameters and return value
- Method must have a docstring following Python conventions (PEP 257)
- Method must be pure in the sense that it only modifies self.tasks
- Method must have no external dependencies

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| task_id | int | Yes | N/A | The unique identifier of the task to delete. Must exist in the task list. |

## Output Format

The method returns a boolean indicating the result of the deletion operation:

```python
True   # Task successfully found and deleted
False  # No task with the given ID exists
```

**Return Value Schema:**
- `True` (boolean): Indicates the task was found and successfully deleted
- `False` (boolean): Indicates no task with the given task_id exists

**Note:** The method does not return the deleted task object to avoid holding references that prevent garbage collection. If the caller needs task data before deletion, they should retrieve it using view_tasks() or a similar method.

## Example Usage

### Delete Existing Task
```python
from todo_manager import TodoManager

# Initialize TodoManager and add tasks
manager = TodoManager()
task1 = manager.add_task("Task 1", "First task")
task2 = manager.add_task("Task 2", "Second task")
task3 = manager.add_task("Task 3", "Third task")

# Delete task with ID 2
result = manager.delete_task(task_id=2)
print(result)
# Output: True

# Verify deletion
tasks = manager.view_tasks()
print(len(tasks))
# Output: 2
print([task['id'] for task in tasks])
# Output: [1, 3]
```

### Delete Non-Existent Task
```python
manager = TodoManager()

# Try to delete a task that doesn't exist
result = manager.delete_task(task_id=999)
print(result)
# Output: False

# Task list remains unchanged
tasks = manager.view_tasks()
print(len(tasks))
# Output: 3 (all original tasks still present)
```

### Delete Task After Retrieving Data
```python
manager = TodoManager()
manager.add_task("Task 1", "Important task")

# Retrieve task before deletion
tasks = manager.view_tasks()
task_to_delete = next((t for t in tasks if t['id'] == 1), None)

if task_to_delete:
    print(f"Deleting: {task_to_delete['title']}")
    # Output: Deleting: Task 1

    # Delete the task
    deleted = manager.delete_task(task_id=1)
    print(f"Deleted: {deleted}")
    # Output: Deleted: True

    # Verify task is gone
    remaining = manager.view_tasks()
    print(f"Remaining tasks: {len(remaining)}")
    # Output: Remaining tasks: 0
```

### Delete Multiple Tasks
```python
manager = TodoManager()
manager.add_task("Task 1")
manager.add_task("Task 2")
manager.add_task("Task 3")
manager.add_task("Task 4")

# Delete tasks in sequence
deleted_count = 0
for task_id in [2, 4]:
    if manager.delete_task(task_id):
        deleted_count += 1

print(f"Deleted {deleted_count} tasks")
# Output: Deleted 2 tasks

# Verify remaining tasks
tasks = manager.view_tasks()
print([task['id'] for task in tasks])
# Output: [1, 3]
```

### Delete Completed Tasks (Batch Operation)
```python
manager = TodoManager()
manager.add_task("Task 1")
manager.add_task("Task 2")
manager.add_task("Task 3")

# Mark task 2 as complete
manager.mark_complete(2)

# Delete all completed tasks
tasks = manager.view_tasks()
completed_ids = [t['id'] for t in tasks if t['completed']]

for task_id in completed_ids:
    manager.delete_task(task_id)

print(f"Deleted {len(completed_ids)} completed tasks")
# Output: Deleted 1 completed task

# Verify only incomplete tasks remain
remaining = manager.view_tasks()
print([t['id'] for t in remaining])
# Output: [1, 3]
```

## Edge Cases

| Edge Case | Description | Handling Strategy |
|-----------|-------------|-------------------|
| Task ID not found | task_id does not match any existing task | Return False (graceful failure, no exception raised) |
| Delete from empty list | self.tasks is empty | Return False (no task to delete) |
| Negative ID | user provides negative task_id (e.g., -1) | Search normally; likely returns False if no matching task |
| Zero ID | user provides 0 as task_id | Search normally; likely returns False if no matching task |
| Very large ID | user provides very large number beyond current IDs | Search normally; returns False if no matching task |
| Duplicate IDs (invalid state) | Multiple tasks have same ID (shouldn't happen) | Delete first match only; ID generation prevents this case |
| Already deleted task | user deletes same task ID twice | First deletion returns True, second returns False |
| Task with completed=True | user deletes a completed task | Allow deletion; completed status irrelevant for deletion |
| Task with empty description | user deletes task with empty description | Allow deletion; description content irrelevant |
| Task with special characters | task title/description contains special chars | Allow deletion; no special handling needed |
| Concurrent deletions | multiple operations deleting same task | Document as thread-unsafe for current scope |
| Delete last remaining task | only one task exists, delete it | Allow deletion; tasks list becomes empty |

## References to Constitution.md

### Principle: Reusable Intelligence
- [CONSTITUTION: PRINCIPLE-REUSABLE-CODE] This skill demonstrates commitment to creating reusable, modular components that can be leveraged across the application
- The DeleteTask method is designed as a self-contained unit with clear inputs/outputs, independent of external dependencies
- Encapsulates task deletion logic for easy reuse in various contexts (CLI, API, tests)
- Simple boolean return value enables easy integration with batch operations and conditional logic

### Principle: Clean Code Standards
- [CONSTITUTION: PRINCIPLE-CLEAN-CODE] Adherence to type hints, docstrings, and single responsibility principle
- Method has one clear purpose: remove a task by ID
- No side effects beyond modifying self.tasks
- Clear, descriptive naming following Python conventions
- No console output ensures reusability across different interfaces

### Principle: Defensive Programming
- [CONSTITUTION: PRINCIPLE-DEFENSIVE-PROGRAMMING] Robust error handling and graceful failure modes
- Does not raise exceptions for non-existent tasks (returns False instead)
- Validates input type before processing
- Handles edge cases gracefully (empty list, invalid IDs)
- No undefined behavior for unexpected inputs

### Principle: Testability
- [CONSTITUTION: PRINCIPLE-TEST-FIRST] Simple input/output contract enables straightforward unit testing
- Boolean return value is easy to verify in tests
- Clear success/failure conditions
- No external dependencies or side effects to mock
- Edge cases are well-defined and testable

## Acceptance Criteria

### AC-001: Delete Existing Task
**Given** a TodoManager with tasks having ids 1, 2, 3
**When** I call delete_task(task_id=2)
**Then** the method returns True
**And** the task list now contains 2 tasks
**And** remaining task IDs are [1, 3]

### AC-002: Delete Non-Existent Task
**Given** a TodoManager with existing tasks (ids 1, 2, 3)
**When** I call delete_task(task_id=999)
**Then** the method returns False
**And** all original tasks remain in the list
**And** the task list still contains 3 tasks

### AC-003: Delete from Empty List
**Given** a TodoManager with no tasks
**When** I call delete_task(task_id=1)
**Then** the method returns False
**And** the task list remains empty

### AC-004: Delete Last Task
**Given** a TodoManager with exactly 1 task with id=1
**When** I call delete_task(task_id=1)
**Then** the method returns True
**And** the task list becomes empty

### AC-005: Delete Completed Task
**Given** a TodoManager with a task with id=1 and completed=True
**When** I call delete_task(task_id=1)
**Then** the method returns True
**And** the task is successfully removed

### AC-006: Delete Task with Empty Description
**Given** a TodoManager with a task with id=1 and description=""
**When** I call delete_task(task_id=1)
**Then** the method returns True
**And** the task is successfully removed

### AC-007: Delete Same Task Twice
**Given** a TodoManager with a task with id=1
**When** I call delete_task(task_id=1) twice
**Then** the first call returns True
**And** the second call returns False
**And** the task list is empty after first call

### AC-008: No Console Output
**Given** a TodoManager with tasks
**When** I call delete_task
**Then** no text is printed to stdout
**And** no text is printed to stderr

### AC-009: _next_id Counter Unchanged
**Given** a TodoManager with 3 tasks and _next_id=4
**When** I call delete_task(task_id=2)
**Then** the _next_id counter remains 4

### AC-010: Remaining Task IDs Unchanged
**Given** a TodoManager with tasks [1, 2, 3, 4]
**When** I delete task 2
**Then** remaining task IDs are [1, 3, 4] (not renumbered)

### AC-011: Delete in Middle of List
**Given** a TodoManager with tasks [1, 2, 3, 4, 5]
**When** I delete task 3
**Then** remaining tasks are [1, 2, 4, 5]
**And** task order is preserved except for the deleted task

### AC-012: Delete First Task
**Given** a TodoManager with tasks [1, 2, 3]
**When** I delete task 1
**Then** remaining tasks are [2, 3]

### AC-013: Delete Last Task
**Given** a TodoManager with tasks [1, 2, 3]
**When** I delete task 3
**Then** remaining tasks are [1, 2]

### AC-014: Type Hints Present
**Given** the DeleteTask method implementation
**When** I inspect the method signature
**Then** type hints are present for:
- task_id: int
- Return type: bool

### AC-015: Docstring Present
**Given** the DeleteTask method implementation
**When** I inspect the method docstring
**Then** it includes:
- Brief description of what the method does
- Documentation for all parameters
- Documentation for return value
- Description of behavior when task not found

## Non-Functional Requirements

### Performance
- Task lookup operation should complete in O(n) time complexity (linear search)
- List removal operation should complete in O(n) time complexity in worst case
- Method should not perform unnecessary operations beyond finding and removing the task

### Maintainability
- Code must be self-documenting with clear variable names
- Method must be easily understandable without external documentation
- Changes to the method should not break backward compatibility without versioning
- Simple boolean return value makes integration straightforward

### Data Integrity
- Deletion must be atomic: the task is either fully removed or not at all
- No partial deletions should occur
- Task IDs must remain stable (no reassignment after deletion)
- Method must not corrupt the task list structure

### Memory Management
- Deleted task object should become eligible for garbage collection
- No references to deleted task should be retained in self.tasks
- Method should not create unnecessary copies of task data

### Scalability Considerations
- In-memory storage is suitable for current scope
- Linear search becomes expensive with large task lists (O(n) lookup)
- Consider optimizing with a dictionary index if task list grows large
- Note that deletions are not persistent across application restarts

## Implementation Notes

### Class Structure
```python
from typing import Dict, Any, List

class TodoManager:
    """Manages a collection of todo tasks."""

    def __init__(self):
        """Initialize an empty task list and ID counter."""
        self.tasks: List[Dict[str, Any]] = []
        self._next_id: int = 1

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the todo list by its ID.

        This method permanently removes a task from the in-memory task list.
        The deletion is irreversible. Task IDs of remaining tasks are not
        reassigned after deletion.

        Args:
            task_id: The unique identifier of the task to delete (required).
                    Must be an integer.

        Returns:
            True if a task with the given ID was found and deleted.
            False if no task with the given ID exists.

        Note:
            This method does not raise exceptions for non-existent tasks.
            Callers should check the return value to determine success.
            The deleted task is not returned; retrieve task data before
            deletion if needed.
        """
        # Implementation to be completed
        pass
```

### Key Implementation Details
1. Iterate through `self.tasks` with index to find task with matching `id`
2. Use list.pop(index) to remove the task if found
3. Return True if task was found and removed
4. Return False if task was not found
5. Do not modify `_next_id` counter
6. No console output (stdout/stderr) should be printed
7. No exceptions should be raised for non-existent tasks

### Implementation Approaches

#### Approach 1: Index-based iteration (Recommended)
```python
for index, task in enumerate(self.tasks):
    if task['id'] == task_id:
        self.tasks.pop(index)
        return True
return False
```

**Pros:**
- Clear and readable
- Efficient removal with pop()
- Early exit on match

**Cons:**
- O(n) search time

#### Approach 2: List comprehension
```python
original_length = len(self.tasks)
self.tasks = [task for task in self.tasks if task['id'] != task_id]
return len(self.tasks) < original_length
```

**Pros:**
- Pythonic and concise
- Single line

**Cons:**
- Creates a new list (less memory efficient)
- Still O(n) but may scan entire list even if task found early

#### Approach 3: Using list.remove() (Not Recommended)
```python
for task in self.tasks:
    if task['id'] == task_id:
        self.tasks.remove(task)
        return True
return False
```

**Pros:**
- Built-in remove method

**Cons:**
- remove() is O(n) even after finding the task
- Less explicit than index-based approach

### Recommended Implementation
Use Approach 1 (index-based iteration) as it provides:
- Clear control flow
- Efficient removal (pop is O(1) from end, O(n) from middle)
- Early exit optimization
- No unnecessary list creation

### Validation Considerations
- Validate task_id is an integer before searching
- Consider whether to raise TypeError for non-integer inputs
- Decide on error handling strategy: raise exception vs return False

**Decision:** For maximum reusability and clean error handling, the spec recommends returning False for non-existent tasks. Type validation can be added to raise TypeError for invalid input types.

### Error Handling Strategy

**Option A: Strict validation (raise exceptions)**
```python
if not isinstance(task_id, int):
    raise TypeError("Task ID must be an integer")
# ... proceed with deletion
```

**Option B: Permissive validation (return False)**
```python
if not isinstance(task_id, int):
    return False
# ... proceed with deletion
```

**Recommendation:** Option A (strict validation) is preferable for:
- Early failure with clear error messages
- Preventing silent failures
- Following Python conventions for type errors
- Making debugging easier

### Batch Deletion Pattern
For deleting multiple tasks based on criteria:
```python
# Example: Delete all completed tasks
def delete_completed_tasks(self) -> int:
    """Delete all completed tasks and return count of deleted tasks."""
    count = 0
    for task in self.tasks[:]:  # Copy to avoid modification during iteration
        if task['completed']:
            self.tasks.remove(task)
            count += 1
    return count
```

This pattern demonstrates how delete_task can be used as a building block for more complex operations.

## Related Features
- AddTask: Create new tasks
- ViewTask: Retrieve a task by ID
- ListTasks: Get all tasks
- MarkTaskComplete: Mark a task as completed
- UpdateTask: Modify task properties

## Change History
| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-01-02 | Spec-Writer | Initial specification for DeleteTask skill |

---

**Status**: Ready for Implementation
**Approver**: TBD
**Implementation Start**: TBD
**Estimated Complexity**: Low
