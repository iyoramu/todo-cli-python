from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class Task:
    id: int
    description: str
    completed: bool = False
    created_at: datetime = datetime.now()
    due_date: datetime = None
    priority: Priority = Priority.MEDIUM

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "priority": self.priority.value
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            description=data["description"],
            completed=data["completed"],
            created_at=datetime.fromisoformat(data["created_at"]),
            due_date=datetime.fromisoformat(data["due_date"]) if data["due_date"] else None,
            priority=Priority(data["priority"])
        )
