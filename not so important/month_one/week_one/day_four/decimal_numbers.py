# create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

float_numbers = [6.666, 7.777, 8.888, 5.555]
new_list = []

for i in float_numbers:
    new_list.append(round(i,2))
print(new_list)
    