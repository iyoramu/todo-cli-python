from typing import List, Dict, Any
from datetime import datetime
from ..models.task import Task

def format_task_for_display(task: Task) -> str:
    status = "✓" if task.completed else "✗"
    due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
    return (
        f"ID: {task.id} | {status} {task.description}\n"
        f"   Priority: {task.priority.value} | Due: {due_date} | Created: {task.created_at.strftime('%Y-%m-%d')}"
    )

def load_tasks_from_json(data: List[Dict[str, Any]]) -> List[Task]:
    return [Task.from_dict(task_data) for task_data in data]

def save_tasks_to_json(tasks: List[Task]) -> List[Dict[str, Any]]:
    return [task.to_dict() for task in tasks]
