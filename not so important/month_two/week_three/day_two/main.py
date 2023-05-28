# class Person:
#     def __init__(self, name: str, surname: str):
#         self.name = name
#         self.surname = surname

#     def say_hello(self) -> None:
#         print(f"hello, {self.name}")


# person = Person(name="first", surname="person")
# person.say_hello()


# def greet_someone(fullname: str) -> None:
#     """Function greets a person given full name as a string"""

#     print(f"Hello {fullname.split()[0]} {fullname.split()[1]}, How are you today?")


# def greet_user(age: int):
#     eligible_to_enter = age > 21

#     if eligible_to_enter:
#         print("Welcome")
#     else:
#         print("Access denied")


# Task Nr.2: Magic Number problem. A number is said to be a magic number,
# if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition.
# If the single digit comes out to be 1,then the number is a magic number.

# For example Number = 50113 => 5+0+1+1+3=10 => 1+0=1 This is a Magic Number

# For example Number = 1234 => 1+2+3+4=10 => 1+0=1 This is a Magic Number

# Write a python function that takes in one parameter - integer and then returns True if number is magic number or False if it is not a magic number


def is_magic_number(number: int) -> bool:
    first_sum = 0
    second_sum = 0
    magic_number = 1

    for number in str(number):
        first_sum = first_sum + int(number)
    if first_sum >= 10:
        for number in str(first_sum):
            second_sum = int(number) + second_sum
        if second_sum == magic_number:
            return True
        return False
    if first_sum == magic_number:
        return True
    return False


magic_number = 1234
not_magic_number = 1234599999999999999999999999
print(is_magic_number(magic_number))
print(is_magic_number(not_magic_number))
