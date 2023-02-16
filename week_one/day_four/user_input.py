# write a program that allows user to write in any float number and then round it.

float_number, decimals = input("Enter a float and decimal points: ").split(",")

print(round(float(float_number), int(decimals)))