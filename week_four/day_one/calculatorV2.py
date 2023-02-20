# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication. Handle all possible errors that may occur.
from typing import Optional

def main():
    
    x = int(input("Enter first integer: "))
    y = int(input("Enter second integer: "))
    sign = input("Enter operator: ")
        
    if sign == "/":
        print(divide_numbers(x, y))
    elif sign == "*":
        print(multiply_numbers(x, y))
    elif sign == "+":
        print(sum_up_numbers(x, y))
    elif sign == "-":
        print(subtraction_of_numbers(x, y))
    else:
        print("Operator does not exist")
    
def divide_numbers(number_one: int | float, number_two: int | float) -> Optional[float]:
    
    try:
        return number_one / number_two
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")
        
def multiply_numbers(number_one: int | float, number_two: int | float) -> Optional[int | float]:

    try:
        return number_one * number_two
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")

def sum_up_numbers(number_one: int | float, number_two: int | float) -> Optional[int | float]: 

    try:
        return number_one + number_two
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")

def subtraction_of_numbers(number_one: int | float, number_two: int | float) -> Optional[int | float]:
    
    try:
        return number_one - number_two
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    main()
