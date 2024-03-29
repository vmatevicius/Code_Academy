from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from modules import User, Task
from typing import Optional, List


class SqliteDatabase:
    def __init__(self, filename: str, base: DeclarativeMeta):
        self.filename = filename
        self.base = base
        self.engine = create_engine(f"sqlite:///{self.filename}")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_database(self) -> None:
        self.base.metadata.create_all(self.engine, checkfirst=True)

    def add_user(self, username: str, password: str) -> None:
        user = User(username=username, password=password)
        self.session.add(user)
        self.session.commit()

    def add_task(self, username: str, task: str) -> None:
        user = self.get_user(username)
        task = Task(task=task)
        user.tasks.append(task)
        self.session.commit()

    def get_user(self, username: str) -> Optional[User]:
        return self.session.query(User).filter_by(username=username).one()

    def update_task(self, task_id: str) -> None:
        task = self.session.query(Task).get(task_id)
        task.completed = True
        self.session.commit()

    def delete_task(self, task_id) -> None:
        task = self.session.query(Task).get(task_id)
        self.session.delete(task)
        self.session.commit()

    def connect_user(self, name: str, password: str) -> bool:
        try:
            user = self.session.query(User).filter_by(username=name).one()
        except:
            return False
        if user.password == password:
            return True
        return False

    def get_user_tasks(self, username: str) -> List[Optional[Task]]:
        user = self.get_user(username)
        return [
            task for task in self.session.query(Task).filter_by(user_id=user.id).all()
        ]

    def get_user(self, name: str) -> Optional[User]:
        return self.session.query(User).filter_by(username=name).one()
