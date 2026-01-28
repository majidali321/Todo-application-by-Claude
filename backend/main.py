from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from contextlib import asynccontextmanager
import os
from src.models import Task, engine, TaskCreate, TaskUpdate
from src.auth import get_current_user
from src.crud import (
    create_task, get_tasks, get_task, update_task,
    delete_task, toggle_complete
)

from typing import List


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/api/{user_id}/tasks")
def list_tasks(user_id: str, current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return get_tasks(session, user_id)


@app.post("/api/{user_id}/tasks")
def create_new_task(user_id: str, task_create: TaskCreate, current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return create_task(session, task_create, user_id)


@app.get("/api/{user_id}/tasks/{task_id}")
def get_single_task(user_id: str, task_id: int, current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return get_task(session, task_id, user_id)


@app.put("/api/{user_id}/tasks/{task_id}")
def update_single_task(user_id: str, task_id: int, task_update: TaskUpdate, current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return update_task(session, task_id, task_update, user_id)


@app.delete("/api/{user_id}/tasks/{task_id}")
def delete_single_task(user_id: str, task_id: int, current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    delete_task(session, task_id, user_id)
    return {"message": "Task deleted successfully"}


@app.patch("/api/{user_id}/tasks/{task_id}/complete")
def toggle_task_complete(user_id: str, task_id: int, current_user: str = Depends(get_current_user), session: Session = Depends(get_session)):
    if current_user != user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return toggle_complete(session, task_id, user_id)


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))