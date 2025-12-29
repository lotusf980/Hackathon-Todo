# Add Task Feature Specification

## Feature Description
The Add Task feature allows users to create new todo items in the application. Each task should have a description and optional metadata such as creation timestamp and completion status.

## Input
- Task description (string): The text content of the task to be added
- Optional priority level (string/integer): Priority of the task (e.g., 'low', 'medium', 'high' or 1-3)
- Optional due date (string): Deadline for the task in YYYY-MM-DD format

## Output
- Success message confirming the task was added
- Task ID (integer): Unique identifier for the newly created task
- Complete task object with all properties (description, ID, status, metadata)

## Rules
1. Task description is required and must not be empty or only whitespace
2. Each task must receive a unique ID that increments from existing tasks
3. New tasks are created with 'incomplete' status by default
4. If no priority is specified, default to 'medium' or 2
5. If no due date is specified, leave as null/empty
6. Duplicate descriptions are allowed (users may need multiple similar tasks)
7. Return appropriate error message if validation fails

## Example Usage
```
Input: add_task('Buy groceries')
Output:
- Message: 'Task "Buy groceries" added successfully'
- ID: 1
- Task: {id: 1, description: 'Buy groceries', status: 'incomplete', priority: 'medium', created_at: '2025-01-01', due_date: null}

Input: add_task('Complete project', priority='high', due_date='2025-01-15')
Output:
- Message: 'Task "Complete project" added successfully'
- ID: 2
- Task: {id: 2, description: 'Complete project', status: 'incomplete', priority: 'high', created_at: '2025-01-01', due_date: '2025-01-15'}
```