from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    create_engine,
    BOOLEAN,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from base import Base

# Create a TO DO list application that runs in terminal.
# It should allow user to log in.
# Each user should have his own tasks in to do list.
# User should be able to add/ update/ delete tasks.
# User information and task information should be kept in database


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column("username", String, nullable=False, unique=True)
    password = Column("password", String)
    tasks = relationship("Task")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    task = Column("task", String)
    completed = Column("completed", BOOLEAN, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
