import pytest
from datetime import datetime
from src.models.task import Task, Priority

def test_task_creation():
    task = Task(
        id=1,
        description="Test task",
        completed=False,
        created_at=datetime(2023, 1, 1),
        due_date=datetime(2023, 12, 31),
        priority=Priority.HIGH
    )
    
    assert task.id == 1
    assert task.description == "Test task"
    assert not task.completed
    assert task.created_at == datetime(2023, 1, 1)
    assert task.due_date == datetime(2023, 12, 31)
    assert task.priority == Priority.HIGH

def test_task_to_dict():
    task = Task(
        id=1,
        description="Test task",
        created_at=datetime(2023, 1, 1),
        due_date=datetime(2023, 12, 31),
        priority=Priority.HIGH
    )
    
    task_dict = task.to_dict()
    assert task_dict["id"] == 1
    assert task_dict["description"] == "Test task"
    assert task_dict["completed"] is False
    assert task_dict["created_at"] == "2023-01-01T00:00:00"
    assert task_dict["due_date"] == "2023-12-31T00:00:00"
    assert task_dict["priority"] == "high"

def test_task_from_dict():
    task_dict = {
        "id": 1,
        "description": "Test task",
        "completed": False,
        "created_at": "2023-01-01T00:00:00",
        "due_date": "2023-12-31T00:00:00",
        "priority": "high"
    }
    
    task = Task.from_dict(task_dict)
    assert task.id == 1
    assert task.description == "Test task"
    assert not task.completed
    assert task.created_at == datetime(2023, 1, 1)
    assert task.due_date == datetime(2023, 12, 31)
    assert task.priority == Priority.HIGH
