# CLI To-Do List App (todo-cli-python)

A modern, professional command-line interface (CLI) to-do list application built with Python.

## Project Structure

```
todo-cli-python/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── todo_manager.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       └── validator.py
├── tests/
│   ├── __init__.py
│   ├── test_todo_manager.py
│   └── test_models.py
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## Features

- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Filter tasks by status (all, completed, pending)
- Set due dates and priorities for tasks
- Persistent storage (JSON file)
- Colorful terminal output
- Command auto-completion
- Comprehensive error handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/iyoramu/todo-cli-python.git
cd todo-cli-python
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Usage

Run the application:
```bash
todo-cli
```

### Available Commands

```
Usage: todo-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add       Add a new task
  list      List all tasks
  complete  Mark task as complete
  delete    Delete a task
  update    Update task details
  clear     Clear all tasks
```

### Examples

Add a new task:
```bash
todo-cli add "Finish project documentation" --due 2025-04-18 --priority high
```

List all tasks:
```bash
todo-cli list
```

Mark task as complete:
```bash
todo-cli complete 1  # Where 1 is the task ID
```

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Building for Distribution

```bash
python setup.py sdist bdist_wheel
```

## Dependencies

- Python 3.8+
- Click (for CLI interface)
- PyYAML (for configuration)
- pytest (for testing)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
