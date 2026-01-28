# Quickstart Guide: CLI Todo Application

**Created**: 2026-01-20
**Feature**: CLI Todo Application
**Target Audience**: Developers and end users

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Command line interface (Terminal on Mac/Linux, Command Prompt or PowerShell on Windows)

### Running the Application

1. Navigate to the project directory:
   ```bash
   cd /path/to/TodoApp
   ```

2. Run the application:
   ```bash
   python src/main.py
   ```

## Available Commands

Once the application is running, you can use the following commands:

### Add a Task
```
add [task_description]
```
Example:
```
add Buy groceries
```

### List All Tasks
```
list
```
Displays all tasks in the format: `[ID] - [Description]`

### Delete a Task
```
delete [ID]
```
Example:
```
delete 1
```

### Exit the Application
```
exit
```
Safely terminates the application

## Example Workflow

1. Start the application: `python src/main.py`
2. Add tasks:
   ```
   add Buy groceries
   add Finish project proposal
   add Call mom
   ```
3. View tasks:
   ```
   list
   ```
   Output:
   ```
   1 - Buy groceries
   2 - Finish project proposal
   3 - Call mom
   ```
4. Delete a task:
   ```
   delete 2
   ```
5. Exit:
   ```
   exit
   ```

## Troubleshooting

- If you get a "command not found" error, ensure Python is installed and in your PATH
- If commands don't work, ensure you're typing them exactly as specified (case-sensitive)
- If you get an error when deleting a task, ensure the ID exists in the current list

## Development Setup

For developers who want to modify the application:

1. Clone the repository
2. Install Python 3.8+
3. Run `python src/main.py` to start the CLI application
4. Make changes to `src/todo_manager.py` for core logic
5. Make changes to `src/main.py` for CLI interface
6. Run tests to ensure functionality remains intact