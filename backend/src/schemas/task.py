from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskResponse(Task):
        id: int

class Config:
    from_attributes = True