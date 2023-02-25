# Generate a dictionary of 10 keys being 1,2,3...10 each of them should store a value of random integer number from 1 to 100.
import random

numbers = {}

keys = 1

while keys < 11:
    numbers[keys] = random.randint(1, 100)
    keys += 1

print(numbers)