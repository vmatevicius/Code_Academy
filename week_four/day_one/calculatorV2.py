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
    
def divide(x: int | float, y: int | float) -> int | float:
    
    try:
        return x / y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")
        
def multiply(x: int | float, y: int | float) -> int | float:

    try:
        return x * y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")

def sum_up(x: int | float, y: int | float) -> int | float: 

    try:
        return x + y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")

def subtraction(x: int | float, y: int | float) -> int | float:
    
    try:
        return x - y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")

if __name__ == "__main__":
    main()
