# Create at least 5 different functions by your own and test it.
import emoji
import math

def count_symbols(string):
    
    symbols = 0
    for symbol in string:
        if symbol == " ":
            continue
        else:
            symbols += 1
    return symbols

print(count_symbols("Hello!"))

def check_if_even(int):
    if int % 2 == 0:
        return True
    else:
        return False
print(check_if_even(4))
print(check_if_even(3))

def check_perfect_square(number):
    
    root = math.sqrt(number)
    if int((root + 0.5)) ** 2 == number:
        return True
    else:
        return False
        
print(check_perfect_square(64))
print(check_perfect_square(63))


def make_emoji(string):

    if "_" in string:
        symbol = emoji.emojize(string)
        return symbol
    else:
        symbol = emoji.emojize(string, language="alias")
        return symbol
    
print(make_emoji(":thumbs_up:"))

def say_hello_to(name):
    
    return f"Hello {name} !"

print(say_hello_to("David"))