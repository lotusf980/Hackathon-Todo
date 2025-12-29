# Update Task Feature Specification

## Feature Description
The Update Task feature allows users to modify existing todo items. Users can update the description, priority, due date, or other metadata of a task while preserving its ID.

## Input
- Task ID (integer): The unique identifier of the task to be updated
- Updated properties (object): One or more properties to update (description, priority, due_date, etc.)
- All properties except Task ID are optional and will only update if provided

## Output
- Success message confirming the task was updated
- Updated task object with all current properties
- Original task object for comparison (optional)

## Rules
1. Task ID must be a valid integer that corresponds to an existing task
2. At least one property must be provided for update
3. If the task ID does not exist, return an appropriate error message
4. Only the specified properties should be updated; others remain unchanged
5. Validation rules for individual properties still apply (e.g., description cannot be empty)
6. Return appropriate error message if validation fails
7. The task ID should never be changed during an update operation

## Example Usage
```
Input: update_task(1, description='Buy groceries and household items', priority='high')
Output:
- Message: 'Task with ID 1 updated successfully'
- Updated task: {id: 1, description: 'Buy groceries and household items', status: 'incomplete', priority: 'high', created_at: '2025-01-01', due_date: null}
- Original task: {id: 1, description: 'Buy groceries', status: 'incomplete', priority: 'medium', created_at: '2025-01-01', due_date: null}

Input: update_task(999, description='Invalid task')
Output:
- Message: 'Error: Task with ID 999 not found'
- Updated task: null
- Original task: null
```