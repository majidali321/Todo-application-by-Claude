import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from todo_manager import TodoManager


def display_tasks(manager: TodoManager) -> None:
    """Display all tasks in the format: [ID] - [Description]"""
    tasks = manager.list_tasks()

    if not tasks:
        print("No tasks.")
        return

    for task in tasks:
        print(f"{task['id']} - {task['description']}")


def main():
    """Run the CLI Todo Application."""
    print("Welcome to the CLI Todo Application!")
    print("Available commands: add, list, delete, exit")

    # Create TodoManager instance
    manager = TodoManager()

    # Main command loop
    while True:
        try:
            # Prompt for command
            user_input = input("> ").strip()

            # Parse command and arguments
            parts = user_input.split(' ', 1)
            command = parts[0].lower()

            if len(parts) > 1:
                args = parts[1]
            else:
                args = ""

            # Add task
            if command == 'add':
                if not args:
                    print("Error: Task description cannot be empty")
                    continue

                try:
                    task = manager.add_task(args)
                    print(f"Added task #{task['id']}: {task['description']}")
                except ValueError as e:
                    print(f"Error: {e}")

            # List all tasks
            elif command == 'list':
                display_tasks(manager)

            # Delete task
            elif command == 'delete':
                if not args:
                    print("Error: Please provide a task ID to delete")
                    continue

                try:
                    task_id = int(args)
                    result = manager.delete_task(task_id)
                    if result:
                        print(f"Deleted task #{task_id}")
                    else:
                        print(f"Error: Task with ID {task_id} not found")
                except ValueError:
                    print(f"Error: Invalid task ID '{args}' - must be a number")
                except TypeError as e:
                    print(f"Error: {e}")

            # Exit application
            elif command == 'exit':
                print("Goodbye!")
                break

            # Unknown command
            else:
                print(f"Unknown command: '{command}'. Available commands: add, list, delete, exit")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
