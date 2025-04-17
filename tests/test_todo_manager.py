import pytest
import json
from datetime import datetime
from pathlib import Path
from src.todo_manager import TodoManager
from src.models.task import Task, Priority

@pytest.fixture
def temp_storage(tmp_path):
    storage = tmp_path / "tasks.json"
    yield storage
    if storage.exists():
        storage.unlink()

def test_add_task(temp_storage):
    manager = TodoManager(str(temp_storage))
    task = manager.add_task("Test task")
    
    assert task.id == 1
    assert task.description == "Test task"
    assert not task.completed
    
    # Verify storage
    with open(temp_storage, "r") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["description"] == "Test task"

def test_complete_task(temp_storage):
    manager = TodoManager(str(temp_storage))
    manager.add_task("Test task")
    
    task = manager.complete_task(1)
    assert task.completed is True
    
    # Verify storage
    with open(temp_storage, "r") as f:
        data = json.load(f)
        assert data[0]["completed"] is True

def test_delete_task(temp_storage):
    manager = TodoManager(str(temp_storage))
    manager.add_task("Test task")
    
    result = manager.delete_task(1)
    assert result is True
    assert len(manager.tasks) == 0
    
    # Verify storage is empty
    with open(temp_storage, "r") as f:
        data = json.load(f)
        assert len(data) == 0

def test_update_task(temp_storage):
    manager = TodoManager(str(temp_storage))
    manager.add_task("Original description")
    
    updated_task = manager.update_task(
        1,
        description="Updated description",
        priority=Priority.HIGH
    )
    
    assert updated_task.description == "Updated description"
    assert updated_task.priority == Priority.HIGH
    
    # Verify storage
    with open(temp_storage, "r") as f:
        data = json.load(f)
        assert data[0]["description"] == "Updated description"
        assert data[0]["priority"] == "high"
