"""
Evolution-of-Todo: Phase I - In-Memory Python Console App

This is the main entry point for the todo application.
The application provides core todo functionality:
- Add Task
- Delete Task
- Update Task
- View Tasks
- Mark Complete

All data is stored in memory only for this phase.
"""

import datetime
from typing import List, Dict, Optional, Any


class Task:
    """Represents a single todo task"""
    def __init__(self, task_id: int, description: str, status: str = 'incomplete',
                 priority: str = 'medium', due_date: Optional[str] = None,
                 created_at: Optional[str] = None, completed_at: Optional[str] = None,
                 completion_notes: Optional[str] = None):
        self.id = task_id
        self.description = description
        self.status = status  # 'incomplete' or 'complete'
        self.priority = priority  # 'low', 'medium', 'high'
        self.due_date = due_date
        self.created_at = created_at or datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.completed_at = completed_at
        self.completion_notes = completion_notes


class TodoApp:
    """Main todo application class"""

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, description: str, priority: str = 'medium', due_date: Optional[str] = None) -> Dict[str, Any]:
        """
        Add a new task to the todo list.
        Specification: specs/add_task.spec.md
        """
        # Validate input: description is required and must not be empty or only whitespace
        if not description or description.strip() == '':
            return {
                'message': 'Error: Task description is required and cannot be empty',
                'task_id': None,
                'task': None
            }

        # Create new task with unique ID
        task_id = self.next_id
        new_task = Task(
            task_id=task_id,
            description=description.strip(),
            status='incomplete',  # Default status
            priority=priority if priority else 'medium',  # Default priority if none provided
            due_date=due_date  # Can be None
        )

        # Add task to list and increment next_id
        self.tasks.append(new_task)
        self.next_id += 1

        # Prepare output as specified
        result_task = {
            'id': new_task.id,
            'description': new_task.description,
            'status': new_task.status,
            'priority': new_task.priority,
            'created_at': new_task.created_at,
            'due_date': new_task.due_date
        }

        return {
            'message': f'Task "{description}" added successfully',
            'task_id': task_id,
            'task': result_task
        }

    def delete_task(self, task_id: int) -> Dict[str, Any]:
        """
        Delete a task from the todo list.
        Specification: specs/delete_task.spec.md
        """
        # Find the task with the given ID
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                # Store the task that will be deleted
                deleted_task = task

                # Remove the task from the list
                del self.tasks[i]

                # Prepare the deleted task object for output
                deleted_task_obj = {
                    'id': deleted_task.id,
                    'description': deleted_task.description,
                    'status': deleted_task.status,
                    'priority': deleted_task.priority,
                    'created_at': deleted_task.created_at,
                    'due_date': deleted_task.due_date
                }

                return {
                    'message': f'Task with ID {task_id} deleted successfully',
                    'task': deleted_task_obj,
                    'remaining_tasks': len(self.tasks)
                }

        # If task ID not found, return error message
        return {
            'message': f'Error: Task with ID {task_id} not found',
            'task': None,
            'remaining_tasks': len(self.tasks)
        }

    def update_task(self, task_id: int, **kwargs) -> Dict[str, Any]:
        """
        Update an existing task.
        Specification: specs/update_task.spec.md
        """
        # Check if at least one property is provided for update
        if not kwargs:
            return {
                'message': 'Error: At least one property must be provided for update',
                'updated_task': None,
                'original_task': None
            }

        # Find the task with the given ID
        for task in self.tasks:
            if task.id == task_id:
                # Store original task for comparison
                original_task = {
                    'id': task.id,
                    'description': task.description,
                    'status': task.status,
                    'priority': task.priority,
                    'created_at': task.created_at,
                    'due_date': task.due_date
                }

                # Update only the specified properties
                for key, value in kwargs.items():
                    if hasattr(task, key):
                        # Apply validation rules - description cannot be empty
                        if key == 'description' and (not value or str(value).strip() == ''):
                            return {
                                'message': 'Error: Description cannot be empty',
                                'updated_task': None,
                                'original_task': original_task
                            }
                        setattr(task, key, value)

                # Prepare updated task object
                updated_task = {
                    'id': task.id,
                    'description': task.description,
                    'status': task.status,
                    'priority': task.priority,
                    'created_at': task.created_at,
                    'due_date': task.due_date
                }

                return {
                    'message': f'Task with ID {task_id} updated successfully',
                    'updated_task': updated_task,
                    'original_task': original_task
                }

        # If task ID not found, return error message
        return {
            'message': f'Error: Task with ID {task_id} not found',
            'updated_task': None,
            'original_task': None
        }

    def view_tasks(self, **filters) -> Dict[str, Any]:
        """
        View all tasks with optional filtering and sorting.
        Specification: specs/view_tasks.spec.md
        """
        # Start with all tasks
        tasks_to_display = []

        # Convert Task objects to dictionaries for output
        for task in self.tasks:
            task_dict = {
                'id': task.id,
                'description': task.description,
                'status': task.status,
                'priority': task.priority,
                'created_at': task.created_at,
                'due_date': task.due_date
            }
            tasks_to_display.append(task_dict)

        # Apply filters if provided
        if filters:
            filtered_tasks = []
            for task in tasks_to_display:
                match = True

                # Check status filter
                if 'status' in filters and filters['status'] != task['status']:
                    match = False

                # Check priority filter
                if 'priority' in filters and filters['priority'] != task['priority']:
                    match = False

                # Check due date before filter
                if 'due_date_before' in filters:
                    due_date = task['due_date']
                    if due_date and due_date > filters['due_date_before']:
                        match = False

                if match:
                    filtered_tasks.append(task)

            tasks_to_display = filtered_tasks

        # Apply sorting if specified
        sort_by = filters.get('sort_by', 'id')  # Default to sorting by ID
        sort_order = filters.get('sort_order', 'asc')  # Default to ascending order

        if sort_by in ['id', 'description', 'status', 'priority', 'created_at', 'due_date']:
            reverse = True if sort_order.lower() == 'desc' else False
            # Handle None values for due_date by treating them as empty strings
            if sort_by == 'due_date':
                tasks_to_display.sort(key=lambda x: (x[sort_by] is None, x[sort_by]), reverse=reverse)
            else:
                tasks_to_display.sort(key=lambda x: x[sort_by] or '', reverse=reverse)

        return {
            'total_tasks': len(tasks_to_display),
            'tasks': tasks_to_display
        }

    def mark_complete(self, task_id: int, notes: Optional[str] = None) -> Dict[str, Any]:
        """
        Mark a task as complete.
        Specification: specs/mark_complete.spec.md
        """
        import datetime

        # Find the task with the given ID
        for task in self.tasks:
            if task.id == task_id:
                # Store original status
                original_status = task.status

                # If task is already complete, return appropriate message
                if task.status == 'complete':
                    return {
                        'message': f'Task with ID {task_id} is already marked as complete',
                        'updated_task': None,
                        'original_status': original_status
                    }

                # Update task status to complete
                task.status = 'complete'
                task.completed_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Add completion notes if provided
                if notes is not None:
                    task.completion_notes = notes

                # Prepare updated task object
                updated_task = {
                    'id': task.id,
                    'description': task.description,
                    'status': task.status,
                    'priority': task.priority,
                    'created_at': task.created_at,
                    'due_date': task.due_date,
                    'completed_at': task.completed_at
                }

                # Include completion notes if they exist
                if hasattr(task, 'completion_notes') and task.completion_notes is not None:
                    updated_task['completion_notes'] = task.completion_notes

                return {
                    'message': f'Task with ID {task_id} marked as complete successfully',
                    'updated_task': updated_task,
                    'original_status': original_status
                }

        # If task ID not found, return error message
        return {
            'message': f'Error: Task with ID {task_id} not found',
            'updated_task': None,
            'original_status': None
        }

    def run(self):
        """Main application loop"""
        print("Welcome to Evolution-of-Todo: Phase I")
        print("Available commands: add, delete, update, view, complete, quit")

        while True:
            command = input("\nEnter command: ").strip().lower()

            if command == 'quit':
                print("Goodbye!")
                break
            elif command == 'add':
                description = input("Enter task description: ").strip()

                # Get optional priority
                priority_input = input("Enter priority (low/medium/high) [default: medium]: ").strip().lower()
                if priority_input in ['low', 'medium', 'high']:
                    priority = priority_input
                else:
                    priority = 'medium'

                # Get optional due date
                due_date_input = input("Enter due date (YYYY-MM-DD) [optional]: ").strip()
                due_date = due_date_input if due_date_input else None

                result = self.add_task(description, priority, due_date)
                print(result['message'])

                if result['task_id']:
                    print(f"Task ID: {result['task_id']}")
            elif command == 'delete':
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    result = self.delete_task(task_id)
                    print(result['message'])

                    if result['task']:
                        print(f"Deleted task: {result['task']['description']}")
                    print(f"Remaining tasks: {result['remaining_tasks']}")
                except ValueError:
                    print("Error: Please enter a valid integer for task ID")
            elif command == 'update':
                try:
                    task_id = int(input("Enter task ID to update: "))

                    print("Enter new values (press Enter to keep current value):")
                    description = input("New description: ").strip()
                    priority = input("New priority (low/medium/high): ").strip().lower()
                    due_date = input("New due date (YYYY-MM-DD): ").strip()

                    # Build update parameters
                    update_kwargs = {}
                    if description:
                        update_kwargs['description'] = description
                    if priority in ['low', 'medium', 'high']:
                        update_kwargs['priority'] = priority
                    if due_date:
                        update_kwargs['due_date'] = due_date

                    # At least one field must be provided for update
                    if not update_kwargs:
                        print("Error: At least one property must be provided for update")
                    else:
                        result = self.update_task(task_id, **update_kwargs)
                        print(result['message'])

                        if result['updated_task']:
                            print(f"Updated task: {result['updated_task']['description']}")
                except ValueError:
                    print("Error: Please enter a valid integer for task ID")
            elif command == 'view':
                print("Options:")
                print("1. View all tasks")
                print("2. Filter by status")
                print("3. Filter by priority")
                view_choice = input("Select option (1-3): ").strip()

                filters = {}
                if view_choice == '2':
                    status = input("Enter status (incomplete/complete): ").strip().lower()
                    if status in ['incomplete', 'complete']:
                        filters['status'] = status
                elif view_choice == '3':
                    priority = input("Enter priority (low/medium/high): ").strip().lower()
                    if priority in ['low', 'medium', 'high']:
                        filters['priority'] = priority

                # Allow sorting if filters are applied
                if filters:
                    sort_choice = input("Sort? (y/n): ").strip().lower()
                    if sort_choice == 'y':
                        sort_by = input("Sort by (id/description/status/priority/created_at/due_date): ").strip()
                        if sort_by in ['id', 'description', 'status', 'priority', 'created_at', 'due_date']:
                            filters['sort_by'] = sort_by
                            order = input("Order (asc/desc): ").strip().lower()
                            if order in ['asc', 'desc']:
                                filters['sort_order'] = order

                result = self.view_tasks(**filters)
                print(f"\nTotal tasks: {result['total_tasks']}")

                if result['tasks']:
                    for task in result['tasks']:
                        due_date_str = task['due_date'] if task['due_date'] else 'No due date'
                        print(f"ID: {task['id']}, Description: {task['description']}, "
                              f"Status: {task['status']}, Priority: {task['priority']}, Due: {due_date_str}")
                else:
                    print("No tasks found.")
            elif command == 'complete':
                try:
                    task_id = int(input("Enter task ID to mark as complete: "))
                    notes_input = input("Enter completion notes (optional): ").strip()
                    notes = notes_input if notes_input else None

                    result = self.mark_complete(task_id, notes)
                    print(result['message'])

                    if result['updated_task']:
                        print(f"Updated task: {result['updated_task']['description']}")
                except ValueError:
                    print("Error: Please enter a valid integer for task ID")
            else:
                print(f"Unknown command: {command}")
                print("Available commands: add, delete, update, view, complete, quit")


def main():
    """Main entry point"""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()