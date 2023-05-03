import modules
from base import Base
from database import SqliteDatabase
from helper_functions import get_valid_number
import getpass
import sys


db = SqliteDatabase("Workers_tasks.db", Base)
db.create_database()

input_first_string = (
    "Select your action: \n1. Register new user \n2. Log in \n3. Exit\n"
)
input_second_string = "Select your action: \n1. Create new task \n2. Update task \n3. Delete task \n4. Get all tasks \n5. Log out \n6. Exit\n"

while True:
    user_input = get_valid_number(3, input_first_string)

    if user_input == 1:
        username = input("Please enter your username:\n")
        password = getpass.getpass("Please enter your password:\n")
        user = modules.User(username=username, password=password)
        db.add_user(user)

    if user_input == 2:
        username = input("Please enter your username:\n")
        password = getpass.getpass("Please enter your password:\n")
        if db.connect_user(name=username, password=password):
            print("Access granted")
            user = db.get_user(name=username)
            while True:
                user_second_input = get_valid_number(6, input_second_string)
                if user_second_input == 1:
                    user_task = input("Enter a task, make text as short as possible: ")
                    db.add_task(username=username, task=user_task)
                    print("Task added succesfully(probably)")
                if user_second_input == 2:
                    finished_task = input("Whick task did you finish?(enter id): ")
                    db.update_task(task_id=finished_task)
                    print("Task updated succesfully(probably)")
                if user_second_input == 3:
                    task_to_delete = input(
                        "Whick task do you want to delete?(enter id): "
                    )
                    db.delete_task(task_id=task_to_delete)
                    print("Task deleted succesfully(probably)")
                if user_second_input == 4:
                    counter = 1
                    print(f" users {username} tasks are: ")
                    for item in db.get_user_tasks(username):
                        print(
                            f"task {counter} - {item.task}, completed = {item.completed}"
                        )
                        counter += 1

                if user_second_input == 5:
                    print("Logging out . . ....")
                    break
                if user_second_input == 6:
                    sys.exit("shutting down . . . ...")
        else:
            print("Wrong username or password")

    if user_input == 3:
        sys.exit("shutting down . . . ...")
