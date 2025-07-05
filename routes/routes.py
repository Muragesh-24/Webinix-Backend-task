from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from scripts.db import get_db
from schemas import TaskCreate, TaskOut, TaskUpdate, TaskStatusRequest
import callbacks.callfunc as callbacks  

router = APIRouter()

@router.post("/tasks", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return callbacks.create_task(db, task)

@router.get("/tasks", response_model=list[TaskOut])
def read_all_tasks(db: Session = Depends(get_db)):
    return callbacks.get_all_tasks(db)

@router.post("/tasks/filter", response_model=list[TaskOut])
def read_tasks_by_status(request: TaskStatusRequest, db: Session = Depends(get_db)):
    if request.status == "completed":
        return callbacks.get_all_completed_tasks(db)
    elif request.status == "incomplete":
        return callbacks.get_all_incomplete_tasks(db)
    else:
        raise HTTPException(status_code=400, detail="Invalid status")

@router.get("/tasks/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = callbacks.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = callbacks.update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    if not callbacks.delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
