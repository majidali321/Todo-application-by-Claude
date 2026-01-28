import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add src to the path so we can import from it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.main import main
from src.todo_manager import TodoManager


class TestCLIInterface(unittest.TestCase):
    """Integration tests for CLI interface."""

    @patch('builtins.input', side_effect=['add Buy groceries', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_command_success(self, mock_stdout, mock_input):
        """Test that the 'add' command successfully adds a task."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Added task #1: Buy groceries", output)
        self.assertIn("Goodbye!", output)

    @patch('builtins.input', side_effect=['add Buy groceries', 'list', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_then_list_command(self, mock_stdout, mock_input):
        """Test that added tasks appear when listing tasks."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Added task #1: Buy groceries", output)
        self.assertIn("1 - Buy groceries", output)

    @patch('builtins.input', side_effect=['add', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_command_empty_description_error(self, mock_stdout, mock_input):
        """Test that the 'add' command shows error for empty description."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Error: Task description cannot be empty", output)

    @patch('builtins.input', side_effect=['add   ', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_command_whitespace_only_description_error(self, mock_stdout, mock_input):
        """Test that the 'add' command shows error for whitespace-only description."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Error: Task description cannot be empty", output)

    @patch('builtins.input', side_effect=['list', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_command_empty_tasks(self, mock_stdout, mock_input):
        """Test that the 'list' command shows 'No tasks.' when no tasks exist."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("No tasks.", output)

    @patch('builtins.input', side_effect=['add First task', 'add Second task', 'list', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_command_multiple_tasks(self, mock_stdout, mock_input):
        """Test that the 'list' command shows all tasks in order."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("1 - First task", output)
        self.assertIn("2 - Second task", output)

    @patch('builtins.input', side_effect=['unknown_command', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown_command_error(self, mock_stdout, mock_input):
        """Test that unknown commands show error message."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Unknown command:", output)
        self.assertIn("Available commands: add, list, delete, exit", output)

    @patch('builtins.input', side_effect=['add Sample task', 'delete 1', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_command_success(self, mock_stdout, mock_input):
        """Test that the 'delete' command successfully deletes a task."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Added task #1: Sample task", output)
        self.assertIn("Deleted task #1", output)

    @patch('builtins.input', side_effect=['delete', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_command_missing_id_error(self, mock_stdout, mock_input):
        """Test that the 'delete' command shows error for missing ID."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Error: Please provide a task ID to delete", output)

    @patch('builtins.input', side_effect=['delete abc', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_command_invalid_id_error(self, mock_stdout, mock_input):
        """Test that the 'delete' command shows error for invalid ID."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Error: Invalid task ID 'abc' - must be a number", output)

    @patch('builtins.input', side_effect=['delete 999', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_command_nonexistent_id_error(self, mock_stdout, mock_input):
        """Test that the 'delete' command shows error for nonexistent ID."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Error: Task with ID 999 not found", output)

    @patch('builtins.input', side_effect=['add Sample task', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_command_ends_program(self, mock_stdout, mock_input):
        """Test that the 'exit' command properly terminates the program."""
        main()

        output = mock_stdout.getvalue()
        self.assertIn("Added task #1: Sample task", output)
        self.assertIn("Goodbye!", output)
        # Verify that the program doesn't continue processing after exit


if __name__ == '__main__':
    unittest.main()