# Write python program that asks user to enter name, surname, age. Put these values into a dictionary and print dictionary

new_dict = {}

name = input("Enter name: ")
surname = input("Enter surname: ")
age = input("Enter age: ")

new_dict["name"] = name
new_dict["surname"] = surname
new_dict["age"] = age

print(new_dict)