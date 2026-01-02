# Updated TodoManager with UpdateTask skill
# Generated from spec: specs/features/update_task.md

from typing import Dict, Any, List, Optional
import copy


class TodoManager:
    """Manages a collection of todo tasks."""

    def __init__(self):
        """Initialize an empty task list and ID counter."""
        self.tasks: List[Dict[str, Any]] = []
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
        # Type validation
        if not isinstance(title, str):
            raise TypeError("Task title must be a string")

        # Strip whitespace from title
        title = title.strip()

        # Empty validation
        if not title:
            raise ValueError("Task title cannot be empty")

        # Create task dictionary
        task = {
            "id": self._next_id,
            "title": title,
            "description": description,
            "completed": False
        }

        # Append to tasks list
        self.tasks.append(task)

        # Increment ID counter for next task
        self._next_id += 1

        # Return the created task
        return task

    def view_tasks(self) -> List[Dict[str, Any]]:
        """
        Retrieve all tasks from the todo list.

        Returns:
            A copy of the list of task dictionaries, where each dictionary
            contains keys: id, title, description, completed.
            Tasks are returned in the order they were added.
            Returns an empty list if no tasks exist.

        Note:
            This method returns a deep copy of the tasks list to prevent
            external modification of internal state.
        """
        return copy.deepcopy(self.tasks)

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
        # Find task by ID
        task_to_update = None
        for task in self.tasks:
            if task['id'] == task_id:
                task_to_update = task
                break

        if task_to_update is None:
            raise ValueError(f"Task with ID {task_id} not found")

        # Validate at least one update field is provided
        if title is None and description is None:
            raise ValueError("At least one field (title or description) must be provided for update")

        # Validate title if provided
        if title is not None:
            if not isinstance(title, str):
                raise TypeError("Task title must be a string")

            # Strip whitespace from title
            title = title.strip()

            if not title:
                raise ValueError("Task title cannot be empty")

            # Update title
            task_to_update['title'] = title

        # Update description if provided
        if description is not None:
            if not isinstance(description, str):
                raise TypeError("Task description must be a string")

            task_to_update['description'] = description

        # Return the updated task
        return task_to_update
