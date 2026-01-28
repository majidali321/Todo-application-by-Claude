from sqlmodel import SQLModel, Field, create_engine
from typing import Optional
from datetime import datetime
import os


class Task(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    user_id: str = Field(index=True)  # from JWT user.id
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None


class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/todo_db")
engine = create_engine(DATABASE_URL)