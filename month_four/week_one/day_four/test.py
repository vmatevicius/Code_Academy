from base import Base
from database import SqliteDatabase

db = SqliteDatabase("Workers_tasks.db", Base)
username = "antanas"

user_task = input("Enter a task, make text as short as possible: ")
db.add_task(username=username, task=user_task)
print("Task added succesfully(probably)")
