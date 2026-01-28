from typing import Dict, Any, List
import copy


class TodoManager:
    """Manages a collection of todo tasks."""

    def __init__(self):
        """Initialize an empty task list and ID counter."""
        self.tasks: List[Dict[str, Any]] = []
        self._next_id: int = 1

    def add_task(self, description: str) -> Dict[str, Any]:
        """
        Add a new task to the todo list.

        Args:
            description: The description of the task (required, must be non-empty).

        Returns:
            A dictionary representing the newly created task with keys:
            - id: Unique integer identifier
            - description: Task description string

        Raises:
            ValueError: If description is empty or contains only whitespace.
            TypeError: If description is not a string type.
        """
        # Type validation
        if not isinstance(description, str):
            raise TypeError("Task description must be a string")

        # Strip whitespace from description
        description = description.strip()

        # Empty validation
        if not description:
            raise ValueError("Task description cannot be empty")

        # Create task dictionary
        task = {
            "id": self._next_id,
            "description": description
        }

        # Append to tasks list
        self.tasks.append(task)

        # Increment ID counter for next task
        self._next_id += 1

        # Return the created task
        return task

    def list_tasks(self) -> List[Dict[str, Any]]:
        """
        Retrieve all tasks from the todo list.

        Returns:
            A copy of the list of task dictionaries, where each dictionary
            contains keys: id, description.
            Tasks are returned in the order they were added.
            Returns an empty list if no tasks exist.

        Note:
            This method returns a deep copy of the tasks list to prevent
            external modification of internal state.
        """
        return copy.deepcopy(self.tasks)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the todo list by its ID.

        This method permanently removes a task from the in-memory task list.
        Task IDs of remaining tasks are not reassigned after deletion.

        Args:
            task_id: The unique identifier of the task to delete. Must be an integer.

        Returns:
            True if a task with the given ID was found and deleted.
            False if no task with the given ID exists.

        Raises:
            TypeError: If task_id is not an integer type.
        """
        # Validate input type
        if not isinstance(task_id, int):
            raise TypeError(f"Task ID must be an integer, got {type(task_id).__name__}")

        # Iterate through tasks and remove matching task
        for index, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(index)
                return True

        # Task not found
        return False
