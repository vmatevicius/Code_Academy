# Write a python program that asks user to enter 3 integers and find the highest value entered.

numbers = []

for i in range(3):
    number = int(input("Enter random number: "))
    numbers.append(number)
print(max(numbers))