# app/schemas.py
from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    description: str
    completed: bool
    priority: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
