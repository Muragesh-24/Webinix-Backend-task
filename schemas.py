from pydantic import BaseModel
from typing import Literal

class TaskCreate(BaseModel):
    name: str
    description: str | None = None
    is_Completed: int = 0

class TaskUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    is_Completed: int | None = None

class TaskOut(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class TaskStatusRequest(BaseModel):
    status: Literal["completed", "incomplete"]
