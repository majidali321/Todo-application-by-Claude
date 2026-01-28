from sqlmodel import Session, select
from models import Task, TaskCreate, TaskUpdate
from fastapi import HTTPException
from typing import List


def create_task(db: Session, task: TaskCreate, user_id: str) -> Task:
    """
    Create a new task for a user
    """
    db_task = Task(
        user_id=user_id,
        title=task.title,
        description=task.description,
        completed=False
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, user_id: str) -> List[Task]:
    """
    Get all tasks for a user
    """
    statement = select(Task).where(Task.user_id == user_id)
    tasks = db.exec(statement).all()
    return tasks


def get_task(db: Session, task_id: int, user_id: str) -> Task:
    """
    Get a specific task by ID for a user
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = db.exec(statement).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


def update_task(db: Session, task_id: int, task_update: TaskUpdate, user_id: str) -> Task:
    """
    Update a specific task for a user
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    db_task = db.exec(statement).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update only provided fields
    if task_update.title is not None:
        db_task.title = task_update.title
    if task_update.description is not None:
        db_task.description = task_update.description
    if task_update.completed is not None:
        db_task.completed = task_update.completed

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, user_id: str):
    """
    Delete a specific task for a user
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    db_task = db.exec(statement).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()


def toggle_complete(db: Session, task_id: int, user_id: str) -> Task:
    """
    Toggle the completed status of a task for a user
    """
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    db_task = db.exec(statement).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.completed = not db_task.completed
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task