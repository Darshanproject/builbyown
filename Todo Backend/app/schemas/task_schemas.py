from pydantic import BaseModel
from datetime import date, time
from uuid import UUID



class CreateTaskSchema(BaseModel):
    category_id: UUID

    title: str
    description: str | None = None
    due_date: date | None = None
    due_time: time | None = None

    priority: str = "medium"

    is_recurring: bool = False
    recurring_type: str | None = None

class UpdateTaskSchema(BaseModel):
    category_id: UUID | None = None
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    completed: bool | None = None

class AssignTaskSchema(BaseModel):
    user_id: UUID