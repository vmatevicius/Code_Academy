# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.
def main():
    
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
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
    
def divide(x: int, y: int) -> float:

    return x / y

def multiply(x, y):

    return x * y

def sum_up(x, y):

    return x + y

def subtraction(x, y):
    
    return x - y

if __name__ == "__main__":
    main()
