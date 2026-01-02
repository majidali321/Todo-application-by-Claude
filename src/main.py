# Enhanced console runner with menu for Add, View, Mark Complete, Update

from todo_manager import TodoManager


def display_tasks(manager: TodoManager) -> None:
    """Display all tasks with completion status indicators."""
    tasks = manager.view_tasks()

    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\n--- Tasks ---")
    for task in tasks:
        status = "[x]" if task['completed'] else "[ ]"
        desc = f" - {task['description']}" if task['description'] else ""
        print(f"{status} [{task['id']}] {task['title']}{desc}")
    print(f"Total: {len(tasks)} task(s)")


def main():
    """Run the TodoApp console interface with menu options."""
    print("=== TodoApp Console ===")
    print("Commands:")
    print("  (a)dd    - Add a new task")
    print("  (v)iew   - View all tasks")
    print("  (m)ark   - Mark a task complete/incomplete")
    print("  (u)pdate - Update a task")
    print("  (q)uit   - Exit the application")
    print()

    # Create TodoManager instance
    manager = TodoManager()

    # Main command loop
    while True:
        try:
            # Prompt for command
            command = input("\nCommand (a/v/m/u/q): ").strip().lower()

            # Add task
            if command == 'a':
                title = input("Task title: ").strip()
                if not title:
                    print("Error: Title cannot be empty")
                    continue

                description = input("Description (optional, press Enter to skip): ").strip()
                task = manager.add_task(title, description)
                print(f"\nTask added with ID: {task['id']}")

            # View tasks
            elif command == 'v':
                display_tasks(manager)

            # Mark task complete/incomplete
            elif command == 'm':
                display_tasks(manager)

                task_id_input = input("\nEnter task ID to toggle: ").strip()
                try:
                    task_id = int(task_id_input)
                    updated_task = manager.mark_complete(task_id)
                    new_status = "complete" if updated_task['completed'] else "incomplete"
                    print(f"\nTask {task_id} marked as {new_status}")
                except ValueError:
                    print(f"Error: Invalid task ID '{task_id_input}' - must be a number")

            # Update task
            elif command == 'u':
                display_tasks(manager)

                task_id_input = input("\nEnter task ID to update: ").strip()
                try:
                    task_id = int(task_id_input)
                except ValueError:
                    print(f"Error: Invalid task ID '{task_id_input}' - must be a number")
                    continue

                title = input("New title (optional, press Enter to skip): ").strip()
                description = input("New description (optional, press Enter to skip): ").strip()

                try:
                    updated_task = manager.update_task(
                        task_id=task_id,
                        title=title if title else None,
                        description=description if description else None
                    )
                    print(f"\nTask {task_id} updated:")
                    print(f"  Title: {updated_task['title']}")
                    print(f"  Description: {updated_task['description'] if updated_task['description'] else '(empty)'}")
                    print(f"  Status: {'Complete' if updated_task['completed'] else 'Incomplete'}")
                except ValueError as e:
                    print(f"\nError: {e}")

            # Quit
            elif command == 'q':
                print("\nExiting...")
                break

            # Unknown command
            else:
                print(f"Unknown command: '{command}' - Use a/v/m/u/q")

        except ValueError as e:
            print(f"\nError: {e}")
        except TypeError as e:
            print(f"\nError: {e}")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")

    # Display final summary
    print(f"\nFinal task count: {len(manager.tasks)}")
    if manager.tasks:
        print("\nAll tasks:")
        display_tasks(manager)


if __name__ == "__main__":
    main()
