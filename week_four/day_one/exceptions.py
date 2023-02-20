# Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.
import sys

def catching_key_exception(dictionary: dict):
    
    try:
        return dictionary["key"]
    except KeyError:
        sys.exit("Key does not exist")
        
def catching_type_error(number: int | float ) -> int | float:
    
    try:
        return number * number
    except TypeError:
        sys.exit("Input is not a number")
        
def catching_zero_division_error(number_one: int | float, number_two: int | float) -> int | float:
    
    try:
        return number_one / number_two
    except ZeroDivisionError:
        sys.exit("Divison by 0 is not available")
        
def catching_name_error(text: str) -> None:
    
    try:
        return calculate_lenght(text)
    except NameError:
        sys.exit("Name is not defined")
        
def catch_keyboard_interrupt_error() -> None:
    
    try:
        while True:
            print("meow")
    except KeyboardInterrupt:
        sys.exit("Program stopped of keyboard interruption")
        