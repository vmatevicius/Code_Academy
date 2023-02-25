# Allow user to enter 10 integers, and then print the sum and average of those entered numbers.

numbers = input("Enter 10 numbers separated by one space: ").split()
new_numbers = []
for number in numbers:
    number = int(number)
    new_numbers.append(number)

print(f"Sum = {sum(new_numbers)} Average = {sum(new_numbers) / 10}")
    