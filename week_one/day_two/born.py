# Create a program that allows user to Enter his/her name and Age
# Calculate the year in which user was born
# Print the answer to the Terminal

age = int(input("Enter your age: "))

name = input("Enter your name: ")

year_born = 2023 - age

print(f"{name} was born in {year_born}")
print(f"{name} was born in", year_born)