import click
from datetime import datetime
from pathlib import Path
from .todo_manager import TodoManager
from .models.task import Task, Priority
from .utils.validator import validate_date, validate_priority
from .utils.helpers import format_task_for_display

@click.group()
@click.version_option("1.0.0")
def cli():
    """A simple CLI To-Do List Application"""
    pass

@cli.command()
@click.argument("description")
@click.option("--due", "due_date", help="Due date (YYYY-MM-DD)")
@click.option("--priority", help="Priority (low, medium, high)", default="medium")
def add(description, due_date, priority):
    """Add a new task"""
    try:
        todo = TodoManager()
        
        due_date_obj = None
        if due_date:
            due_date_obj = validate_date(due_date)
        
        priority_enum = Priority(validate_priority(priority))
        
        task = todo.add_task(description, due_date_obj, priority_enum)
        click.echo(f"Added task: {format_task_for_display(task)}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
@click.option("--all", "show_all", is_flag=True, help="Show all tasks including completed")
def list(show_all):
    """List all tasks"""
    todo = TodoManager()
    tasks = todo.list_tasks(show_all)
    
    if not tasks:
        click.echo("No tasks found.")
        return
    
    for task in tasks:
        click.echo(format_task_for_display(task))

@cli.command()
@click.argument("task_id", type=int)
def complete(task_id):
    """Mark a task as complete"""
    todo = TodoManager()
    task = todo.complete_task(task_id)
    
    if task:
        click.echo(f"Task {task_id} marked as complete.")
    else:
        click.echo(f"Task {task_id} not found.", err=True)

@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    """Delete a task"""
    todo = TodoManager()
    if todo.delete_task(task_id):
        click.echo(f"Task {task_id} deleted.")
    else:
        click.echo(f"Task {task_id} not found.", err=True)

@cli.command()
@click.argument("task_id", type=int)
@click.option("--description", help="New task description")
@click.option("--due", "due_date", help="New due date (YYYY-MM-DD)")
@click.option("--priority", help="New priority (low, medium, high)")
def update(task_id, description, due_date, priority):
    """Update a task"""
    try:
        todo = TodoManager()
        
        due_date_obj = validate_date(due_date) if due_date else None
        priority_enum = Priority(validate_priority(priority)) if priority else None
        
        task = todo.update_task(
            task_id,
            description,
            due_date_obj,
            priority_enum
        )
        
        if task:
            click.echo(f"Updated task: {format_task_for_display(task)}")
        else:
            click.echo(f"Task {task_id} not found.", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
def clear():
    """Clear all tasks"""
    if click.confirm("Are you sure you want to delete all tasks?"):
        todo = TodoManager()
        todo.clear_tasks()
        click.echo("All tasks have been cleared.")

if __name__ == "__main__":
    cli()
