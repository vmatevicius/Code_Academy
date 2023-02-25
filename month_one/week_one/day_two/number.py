# Create a program that expects user to enter two numbers
# multiply those numbers and print the answer
# Create similar programs with other signs.

def main():
    
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    sign = input("Enter operator: ")
    if sign == "/":
        print(division(x,y))
    elif sign == "*":
        print(multiply(x,y))
    elif sign == "+":
        print(sum(x,y))
    else:
        print("Operator does not exist")

def division(x,y):

    return x / y

def multiply(x,y):

    return x * y

def sum(x,y):

    return x + y

if __name__ == "__main__":
    main()