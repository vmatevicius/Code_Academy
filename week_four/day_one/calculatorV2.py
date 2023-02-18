# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication. Handle all possible errors that may occur.

import sys

def main():
    
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    sign = input("Enter operator: ")
        
    if sign == "/":
        print(divide(x, y))
    elif sign == "*":
        print(multiply(x, y))
    elif sign == "+":
        print(sum_up(x, y))
    elif sign == "-":
        print(subtraction(x, y))
    else:
        print("Operator does not exist")
    
def divide(x, y):
    
    try:
        return round(float(x) / float(y), 2)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
        
def multiply(x, y):

    try:
        return round(float(x) * float(y), 2)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")

def sum_up(x, y):

    try:
        return round(float(x) + float(y), 1)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")

def subtraction(x, y):
    
    try:
        return round(float(x) - float(y), 1)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")

if __name__ == "__main__":
    main()
