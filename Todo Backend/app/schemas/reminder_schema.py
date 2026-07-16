from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class CreateReminderSchema(BaseModel):
    task_id: UUID
    title: str
    remind_at: datetime
    recurring_type: str = "once"

class UpdateReminderSchema(BaseModel):
    title: str | None = None
    reminder_time: datetime | None = None
    recurring_type: str | None = None