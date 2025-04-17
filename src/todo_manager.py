import json
from pathlib import Path
from typing import List, Optional
from datetime import datetime
from .models.task import Task, Priority
from .utils.helpers import load_tasks_from_json, save_tasks_to_json, format_task_for_display

class TodoManager:
    def __init__(self, storage_path: str = "tasks.json"):
        self.storage_path = Path(storage_path)
        self.tasks: List[Task] = []
        self._load_tasks()

    def _load_tasks(self):
        if self.storage_path.exists():
            with open(self.storage_path, "r") as f:
                data = json.load(f)
                self.tasks = load_tasks_from_json(data)
        else:
            self.tasks = []

    def _save_tasks(self):
        with open(self.storage_path, "w") as f:
            json.dump(save_tasks_to_json(self.tasks), f, indent=2)

    def add_task(self, description: str, due_date: datetime = None, priority: Priority = Priority.MEDIUM) -> Task:
        new_id = max((task.id for task in self.tasks), default=0) + 1
        task = Task(
            id=new_id,
            description=description,
            due_date=due_date,
            priority=priority
        )
        self.tasks.append(task)
        self._save_tasks()
        return task

    def list_tasks(self, show_completed: bool = True) -> List[Task]:
        if show_completed:
            return self.tasks
        return [task for task in self.tasks if not task.completed]

    def complete_task(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self._save_tasks()
                return task
        return None

    def delete_task(self, task_id: int) -> bool:
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) != initial_count:
            self._save_tasks()
            return True
        return False

    def update_task(
        self,
        task_id: int,
        description: str = None,
        due_date: datetime = None,
        priority: Priority = None
    ) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if priority:
                    task.priority = priority
                self._save_tasks()
                return task
        return None

    def clear_tasks(self):
        self.tasks = []
        self._save_tasks()
