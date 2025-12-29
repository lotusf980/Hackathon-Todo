# Evolution-of-Todo: Phase I

## Overview
Evolution-of-Todo is a progressive todo application that evolves from a simple in-memory console application to a full-featured web application. Phase I implements the core functionality as an in-memory Python console application.

## Features
- Add new tasks with descriptions and optional metadata
- Delete existing tasks
- Update task details
- View all tasks with filtering and sorting options
- Mark tasks as complete

## Requirements
- Python 3.8 or higher

## Setup Instructions

1. Clone or download this repository to your local machine

2. Navigate to the project directory:
   ```bash
   cd Evolution-of-Todo
   ```

3. Run the application:
   ```bash
   python src/main.py
   ```

## Usage
Once the application is running, you can use the following commands:

- `add` - Add a new task
- `delete` - Delete an existing task
- `update` - Update an existing task
- `view` - View all tasks
- `complete` - Mark a task as complete
- `quit` - Exit the application

## Project Structure
```
Evolution-of-Todo/
├── .specify/
│   └── memory/
│       └── constitution.md          # Project constitution
├── specs/                         # Feature specifications
│   ├── add_task.spec.md
│   ├── delete_task.spec.md
│   ├── update_task.spec.md
│   ├── view_tasks.spec.md
│   └── mark_complete.spec.md
├── src/                           # Source code
│   └── main.py                    # Main application entry point
├── README.md                      # This file
└── CLAUDE.md                      # Claude Code CLI instructions
```

## Development
This project follows Spec-Driven Development (SDD) methodology. All features are implemented based on the specifications in the `specs/` directory. Each feature specification includes detailed input/output definitions, rules, and example usage.

## Next Steps
Phase II will introduce persistent storage, Phase III will add a web interface, and subsequent phases will continue to evolve the application with additional features and capabilities.