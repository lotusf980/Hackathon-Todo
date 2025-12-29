# Claude Code Rules

This file provides instructions for generating code from specifications using Claude Code CLI for the Evolution-of-Todo project.

## Project Context

**Project Name:** Evolution-of-Todo
**Phase:** I – In-Memory Python Console App
**Approach:** Spec-Driven Development (SDD)

## Claude Code CLI Instructions

### 1. Code Generation from Specifications
When implementing features for the Evolution-of-Todo project, always refer to the specifications in the `specs/` directory:

- `specs/add_task.spec.md` - Add Task feature specification
- `specs/delete_task.spec.md` - Delete Task feature specification
- `specs/update_task.spec.md` - Update Task feature specification
- `specs/view_tasks.spec.md` - View Tasks feature specification
- `specs/mark_complete.spec.md` - Mark Complete feature specification

### 2. Implementation Process
1. **Read the specification** for the feature you're implementing
2. **Understand the input/output requirements** and rules
3. **Implement the feature** in `src/main.py` following the specification
4. **Update the implementation** to remove TODO comments and implement the functionality
5. **Test the feature** against the example usage in the specification

### 3. Code Generation Commands
To generate code for a specific feature based on its specification:

```bash
# Generate code for add_task functionality
claude-code "Implement the add_task method in src/main.py based on specs/add_task.spec.md"

# Generate code for delete_task functionality
claude-code "Implement the delete_task method in src/main.py based on specs/delete_task.spec.md"

# Generate code for update_task functionality
claude-code "Implement the update_task method in src/main.py based on specs/update_task.spec.md"

# Generate code for view_tasks functionality
claude-code "Implement the view_tasks method in src/main.py based on specs/view_tasks.spec.md"

# Generate code for mark_complete functionality
claude-code "Implement the mark_complete method in src/main.py based on specs/mark_complete.spec.md"
```

### 4. Development Workflow
1. **Start with specifications** - Always implement features based on the specs in the `specs/` directory
2. **Follow the SDD approach** - Specification first, then implementation
3. **Maintain consistency** - Ensure your implementation matches the specification exactly
4. **Preserve architecture** - Keep the class structure and method signatures as defined in `src/main.py`
5. **Update TODOs** - Replace all TODO comments with actual implementation code

### 5. Code Quality Guidelines
- Follow Python PEP 8 style guidelines
- Maintain type hints where specified
- Include appropriate error handling as defined in specifications
- Write clear, readable code that matches the specification requirements
- Preserve the existing class structure in `TodoApp`

### 6. Verification Process
After implementing each feature:
1. Verify that your implementation matches the specification
2. Test with the example usage scenarios provided in the spec
3. Ensure all input/output requirements are met
4. Validate that all rules defined in the specification are enforced

### 7. Project Evolution
This is Phase I of the Evolution-of-Todo project. Keep the architecture modular and extensible for future phases that will include:
- Phase II: Persistent storage
- Phase III: Web interface
- Future phases: Additional features and capabilities

Remember: The specifications in the `specs/` directory are the source of truth for all feature implementations.