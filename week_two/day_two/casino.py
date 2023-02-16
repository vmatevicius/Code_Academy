# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

user = {}

user["name"] = name
user["surname"] = surname
user["age"] = age

if user["age"] < 21:
    print("You are under age")
else:
    print("You are allowed to enter")
    
