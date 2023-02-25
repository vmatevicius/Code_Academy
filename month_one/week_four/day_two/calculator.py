# Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.
from calculator_functions import *

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