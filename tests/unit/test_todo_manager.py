import unittest
from src.todo_manager import TodoManager


class TestTodoManager(unittest.TestCase):
    """Unit tests for TodoManager class."""

    def setUp(self):
        """Set up a fresh TodoManager instance for each test."""
        self.manager = TodoManager()

    def test_add_task_success(self):
        """Test adding a task with a valid description."""
        description = "Buy groceries"

        result = self.manager.add_task(description)

        # Verify the returned task has correct structure
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["description"], "Buy groceries")

        # Verify the task was added to the internal list
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["id"], 1)
        self.assertEqual(tasks[0]["description"], "Buy groceries")

    def test_add_task_empty_description(self):
        """Test that adding a task with empty description raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.manager.add_task("")

        self.assertIn("cannot be empty", str(context.exception))

    def test_add_task_whitespace_only_description(self):
        """Test that adding a task with whitespace-only description raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.manager.add_task("   ")

        self.assertIn("cannot be empty", str(context.exception))

    def test_add_task_non_string_description(self):
        """Test that adding a task with non-string description raises TypeError."""
        with self.assertRaises(TypeError) as context:
            self.manager.add_task(123)

        self.assertIn("must be a string", str(context.exception))

    def test_add_multiple_tasks_unique_ids(self):
        """Test that adding multiple tasks assigns unique IDs."""
        task1 = self.manager.add_task("First task")
        task2 = self.manager.add_task("Second task")
        task3 = self.manager.add_task("Third task")

        # Verify IDs are assigned sequentially
        self.assertEqual(task1["id"], 1)
        self.assertEqual(task2["id"], 2)
        self.assertEqual(task3["id"], 3)

        # Verify all tasks are stored
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 3)

    def test_add_task_trims_whitespace(self):
        """Test that leading and trailing whitespace is trimmed from description."""
        result = self.manager.add_task("  Buy groceries  ")

        self.assertEqual(result["id"], 1)
        self.assertEqual(result["description"], "Buy groceries")

    def test_list_tasks_empty_initially(self):
        """Test that list_tasks returns an empty list initially."""
        tasks = self.manager.list_tasks()

        self.assertEqual(tasks, [])

    def test_list_tasks_returns_copy(self):
        """Test that list_tasks returns a copy of the internal list."""
        self.manager.add_task("Sample task")

        tasks = self.manager.list_tasks()
        tasks.append({"id": 999, "description": "Fake task"})

        # Original internal list should not be affected by modification to returned list
        current_tasks = self.manager.list_tasks()
        self.assertEqual(len(current_tasks), 1)
        self.assertNotEqual(current_tasks[0]["id"], 999)

    def test_list_tasks_returns_all_added_tasks(self):
        """Test that list_tasks returns all added tasks."""
        self.manager.add_task("First task")
        self.manager.add_task("Second task")

        tasks = self.manager.list_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["id"], 1)
        self.assertEqual(tasks[0]["description"], "First task")
        self.assertEqual(tasks[1]["id"], 2)
        self.assertEqual(tasks[1]["description"], "Second task")

    def test_delete_task_exists_and_return_true(self):
        """Test that delete_task returns True when task exists and deletes it."""
        self.manager.add_task("Sample task")

        result = self.manager.delete_task(1)

        self.assertTrue(result)

        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_task_not_exists_and_return_false(self):
        """Test that delete_task returns False when task doesn't exist."""
        result = self.manager.delete_task(1)

        self.assertFalse(result)

        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_delete_specific_task_from_multiple(self):
        """Test that delete_task removes only the specified task from multiple tasks."""
        self.manager.add_task("First task")
        self.manager.add_task("Second task")
        self.manager.add_task("Third task")

        result = self.manager.delete_task(2)  # Delete middle task

        self.assertTrue(result)

        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]["id"], 1)
        self.assertEqual(tasks[0]["description"], "First task")
        self.assertEqual(tasks[1]["id"], 3)
        self.assertEqual(tasks[1]["description"], "Third task")

    def test_delete_task_invalid_id_type_raises_error(self):
        """Test that delete_task raises TypeError for non-integer ID."""
        with self.assertRaises(TypeError) as context:
            self.manager.delete_task("invalid_id")

        self.assertIn("must be an integer", str(context.exception))

    def test_delete_task_preserves_remaining_ids(self):
        """Test that deleting a task doesn't affect IDs of remaining tasks."""
        self.manager.add_task("First task")
        self.manager.add_task("Second task")
        self.manager.add_task("Third task")

        # Delete first task
        self.manager.delete_task(1)

        # Add another task - it should get ID 4, not reuse ID 1
        new_task = self.manager.add_task("Fourth task")

        self.assertEqual(new_task["id"], 4)

        tasks = self.manager.list_tasks()
        ids = [task["id"] for task in tasks]
        self.assertNotIn(1, ids)  # Original ID 1 should not reappear
        self.assertIn(2, ids)  # ID 2 should still exist
        self.assertIn(3, ids)  # ID 3 should still exist
        self.assertIn(4, ids)  # New task should have ID 4


if __name__ == '__main__':
    unittest.main()