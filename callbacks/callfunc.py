from sqlalchemy.orm import Session
from models.task import Task
from schemas import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_all_tasks(db: Session):
    return db.query(Task).all()

def get_all_completed_tasks(db: Session):
    return db.query(Task).filter(Task.is_Completed == 1).all()

def get_all_incomplete_tasks(db: Session):
    return db.query(Task).filter(Task.is_Completed == 0).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, update_data: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False
