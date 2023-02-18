# Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.
import sys

def catching_key_exception(dictionary):
    
    try:
        return dictionary["key"]
    except KeyError:
        sys.exit("Key does not exist")
    
def catching_type_error(number):
    
    try:
        return number * number
    except TypeError:
        sys.exit("Input is not a number")
        
def catching_zero_division_error(number):
    
    try:
        return 50 / number
    except ZeroDivisionError:
        sys.exit("Divison by 0 is not available")
        
def catching_name_error(text):
    
    try:
        return calculate_lenght(text)
    except NameError:
        sys.exit("Name is not defined")
        
def catch_keyboard_interrupt_error():
    
    try:
        while True:
            print("meow")
    except KeyboardInterrupt:
        sys.exit("Program stopped of keyboard interruption")
        