# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
# You can use input to receive the number. Example:
# n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n = int(input("Enter a number: "))
i = 1
numbers = {}
for _ in range(n):
    j = i * i
    numbers[i] = j
    i += 1 
print(numbers)
