# Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.
from typing import Optional
import sys

def greet_someone(name: str= "Human") -> Optional[str]:
    
    try:
        return f"Hello {name}"
    except Exception as e:
        sys.exit(f"Error : {e}")

# print(greet_someone())
        
def multiply_numbers(number_one: int | float, number_two: int | float ) -> Optional[int | float]:
    
    try:
        return number_one * number_two
    except TypeError:
        print("Input is not a number")
        
# multiply("cat")
        
def divide_numbers(number_one: int | float, number_two: int | float) -> Optional[int | float]:
    
    try:
        return number_one / number_two
    except ZeroDivisionError:
        print("Divison by 0 is not available")
        
# divide(5,0)
        
def verify_user(username: str) -> Optional[bool]:
    
    VALID_USERNAME = "Antanas"
    try:
        if username == valid_username:
            return True
        return False
    except NameError:
        print("Name is not defined")
        
# print(verify_user("Antanas"))

def uppercase_user_input() -> Optional[str]:
    
    try:
        user_input = input("Enter anything: ")
        return user_input.upper()
    except KeyboardInterrupt:
        print("\n Program stopped of keyboard interruption")

# print(uppercase_user_input())
        