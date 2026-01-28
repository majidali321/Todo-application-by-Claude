# Skills and Subagents for TodoApp - Reusable Intelligence Framework

## Reusable Intelligence: Agent Skills

### Constitution for Skills
- **Principles**: All skills must be reusable, modular, and spec-driven
- **Design**: Follow clean interfaces with clear inputs/outputs
- **Integration**: Skills should enhance existing Todo app functionality
- **Scalability**: Skills should support future features and extensions

## Defined Skills

### Skill 1: Task Creation Skill
- **Description**: Parses user input and creates new todo tasks with proper validation
- **Inputs**:
  - task_title (string): Title of the task
  - task_description (string, optional): Detailed description of the task
  - priority (string, optional): Priority level (low, medium, high)
  - due_date (string, optional): Due date in YYYY-MM-DD format
  - user_id (string): ID of the user creating the task
- **Outputs**:
  - success (boolean): Whether the task was created successfully
  - task_id (string): Unique identifier of the created task
  - message (string): Status message
- **Example**:
  ```
  Input: {task_title: "Buy groceries", user_id: "user123", priority: "high"}
  Output: {success: true, task_id: "task456", message: "Task created successfully"}
  ```

### Skill 2: Task Update Skill
- **Description**: Updates existing todo tasks with validation and user authorization checks
- **Inputs**:
  - task_id (string): Unique identifier of the task to update
  - user_id (string): ID of the user requesting the update
  - updates (object): Object containing fields to update (title, description, completed, priority, etc.)
- **Outputs**:
  - success (boolean): Whether the update was successful
  - message (string): Status message
  - updated_task (object): The updated task object
- **Example**:
  ```
  Input: {task_id: "task456", user_id: "user123", updates: {completed: true}}
  Output: {success: true, message: "Task updated successfully", updated_task: {...}}
  ```

### Skill 3: Natural Language Parser
- **Description**: Interprets natural language commands and converts them into structured task operations
- **Inputs**:
  - command (string): Natural language input from user
  - user_id (string): ID of the user issuing the command
- **Outputs**:
  - intent (string): Detected intent (create, update, delete, list, etc.)
  - parameters (object): Extracted parameters from the command
  - confidence (float): Confidence level of the interpretation
- **Example**:
  ```
  Input: {command: "Add a task to buy milk by tomorrow", user_id: "user123"}
  Output: {intent: "create", parameters: {title: "buy milk", due_date: "2026-01-29"}, confidence: 0.95}
  ```

### Skill 4: Priority Assignment Skill
- **Description**: Automatically assigns priority levels based on due dates, keywords, and context
- **Inputs**:
  - task_title (string): Title of the task
  - task_description (string): Description of the task
  - due_date (string, optional): Due date of the task
  - user_preferences (object, optional): User's priority preferences
- **Outputs**:
  - priority (string): Assigned priority level (low, medium, high, urgent)
  - reasoning (string): Explanation for the priority assignment
- **Example**:
  ```
  Input: {task_title: "Fix critical bug", due_date: "2026-01-29"}
  Output: {priority: "urgent", reasoning: "Contains critical keywords and near due date"}
  ```

### Skill 5: Recurring Task Handler
- **Description**: Creates and manages recurring tasks based on specified patterns
- **Inputs**:
  - base_task (object): Base task configuration
  - recurrence_pattern (string): Pattern (daily, weekly, monthly, yearly)
  - recurrence_end (string, optional): End condition (date or occurrence count)
  - user_id (string): ID of the user creating the recurring task
- **Outputs**:
  - success (boolean): Whether the recurring task was set up successfully
  - instances_created (number): Number of initial instances created
  - schedule_id (string): Unique identifier for the recurrence schedule
- **Example**:
  ```
  Input: {base_task: {title: "Weekly team meeting"}, recurrence_pattern: "weekly", user_id: "user123"}
  Output: {success: true, instances_created: 1, schedule_id: "sched789"}
  ```

### Skill 6: Task Search and Filtering Skill
- **Description**: Searches and filters tasks based on various criteria
- **Inputs**:
  - filters (object): Object containing filter criteria (status, priority, date range, keywords)
  - user_id (string): ID of the user requesting the search
  - limit (number, optional): Maximum number of results to return
  - offset (number, optional): Offset for pagination
- **Outputs**:
  - tasks (array): Array of matching task objects
  - total_count (number): Total number of matching tasks
  - applied_filters (object): Filters that were applied
- **Example**:
  ```
  Input: {filters: {priority: "high", status: "incomplete"}, user_id: "user123"}
  Output: {tasks: [...], total_count: 5, applied_filters: {priority: "high", status: "incomplete"}}
  ```

## Subagents

### Subagent 1: CRUD Subagent
- **Purpose**: Handles all database operations for task management
- **Capabilities**:
  - Create, read, update, delete tasks
  - Batch operations for efficiency
  - Transaction management
  - Data validation and sanitization
- **Interface**:
  - `create_task(task_data, user_id)`
  - `read_tasks(user_id, filters)`
  - `update_task(task_id, user_id, updates)`
  - `delete_task(task_id, user_id)`
  - `batch_update(task_ids, user_id, updates)`
- **Usage**: Called by other skills and services when database operations are needed
- **Example**:
  ```
  CRUD_Subagent.create_task({
    title: "New Task",
    description: "Task description",
    user_id: "user123"
  })
  ```

### Subagent 2: Auth Subagent
- **Purpose**: Manages authentication and authorization for user access control
- **Capabilities**:
  - User authentication and session management
  - Permission validation for task operations
  - User isolation enforcement
  - Token generation and validation
- **Interface**:
  - `authenticate_user(credentials)`
  - `validate_user_permission(user_id, task_id, operation)`
  - `create_session(user_id)`
  - `invalidate_session(session_token)`
- **Usage**: Ensures users can only access their own tasks
- **Example**:
  ```
  Auth_Subagent.validate_user_permission("user123", "task456", "read")
  ```

### Subagent 3: Natural Language Processing Subagent
- **Purpose**: Advanced NLP for understanding complex task commands and intents
- **Capabilities**:
  - Intent recognition for task operations
  - Entity extraction (dates, priorities, categories)
  - Sentiment analysis for priority inference
  - Multi-language support
- **Interface**:
  - `parse_command(command_text)`
  - `extract_entities(text)`
  - `determine_intent(text)`
  - `analyze_sentiment(text)`
- **Usage**: Powers the chatbot interface and voice commands
- **Example**:
  ```
  NLP_Subagent.parse_command("Remind me to call John about the project tomorrow at 3 PM")
  ```

### Subagent 4: Notification Subagent
- **Purpose**: Manages task reminders and notifications
- **Capabilities**:
  - Schedule and send reminders
  - Handle multiple notification channels (email, push, SMS)
  - Manage notification preferences
  - Track notification delivery status
- **Interface**:
  - `schedule_reminder(task_id, user_id, time)`
  - `send_notification(user_id, message, channel)`
  - `update_preferences(user_id, preferences)`
  - `cancel_reminder(notification_id)`
- **Usage**: Sends timely reminders for upcoming tasks
- **Example**:
  ```
  Notification_Subagent.schedule_reminder("task456", "user123", "2026-01-29T15:00:00Z")
  ```

## Usage Examples

### Example 1: Creating a Task via Chat Interface
```
User: "Add a high priority task to prepare quarterly report by Friday"
Chatbot → Natural Language Parser → Task Creation Skill → CRUD Subagent
Result: New task created with high priority and Friday due date
```

### Example 2: Updating Task Status
```
User: "Mark my meeting prep task as completed"
Chatbot → Natural Language Parser → Task Search Skill → Task Update Skill → CRUD Subagent
Result: Matching task found and updated to completed status
```

### Example 3: Setting Up Recurring Task
```
User: "I need to workout every Monday and Wednesday"
Chatbot → Natural Language Parser → Recurring Task Handler → CRUD Subagent
Result: Recurring workout tasks scheduled for Mondays and Wednesdays
```

## Integration Points

### With Existing Todo App
- Skills integrate with existing CRUD operations in `src/todo_manager.py`
- Subagents connect to existing database models in `backend/src/models.py`
- Authentication skills work with existing auth system in `backend/src/auth.py`
- Natural language skills enhance CLI interface in `src/main.py`

### For Future Phases
- Skills provide foundation for AI chatbot in Phase III
- Subagents enable scalable architecture for additional features
- Modular design supports easy extension and maintenance
- Standardized interfaces ensure consistent behavior across implementations