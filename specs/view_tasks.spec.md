# View Tasks Feature Specification

## Feature Description
The View Tasks feature allows users to see all tasks in the todo list. The feature should display tasks with their current status, priority, and other relevant metadata in a clear, organized format.

## Input
- Optional filter parameters (object): Criteria to filter tasks (e.g., status='completed', priority='high', due_date_before='2025-01-31')
- Optional sorting parameters (object): Criteria to sort tasks (e.g., sort_by='priority', sort_order='desc')

## Output
- List of all tasks (or filtered tasks) with complete details
- Total count of tasks displayed
- Formatted display suitable for console output

## Rules
1. If no filters are applied, return all tasks in the system
2. Tasks should be displayed with ID, description, status, priority, and due date
3. If filters are applied, only return tasks that match the criteria
4. Sorting should be applied after filtering if both are specified
5. Return empty list if no tasks match the filter criteria
6. Default sorting should be by task ID in ascending order
7. Display format should be user-friendly and readable in console

## Example Usage
```
Input: view_tasks()
Output:
- Total tasks: 3
- Tasks: [
    {id: 1, description: 'Buy groceries', status: 'incomplete', priority: 'medium', created_at: '2025-01-01', due_date: null},
    {id: 2, description: 'Complete project', status: 'incomplete', priority: 'high', created_at: '2025-01-01', due_date: '2025-01-15'},
    {id: 3, description: 'Call mom', status: 'complete', priority: 'low', created_at: '2025-01-01', due_date: '2025-01-10'}
  ]

Input: view_tasks(status='incomplete', sort_by='priority', sort_order='desc')
Output:
- Total tasks: 2
- Tasks: [
    {id: 2, description: 'Complete project', status: 'incomplete', priority: 'high', created_at: '2025-01-01', due_date: '2025-01-15'},
    {id: 1, description: 'Buy groceries', status: 'incomplete', priority: 'medium', created_at: '2025-01-01', due_date: null}
  ]
```