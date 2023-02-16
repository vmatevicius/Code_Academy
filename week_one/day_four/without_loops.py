# # create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

float_numbers = [6.666, 7.777, 8.888, 5.555]
a, b, c, d = float_numbers
new_list = [round(a,2),round(b,2),round(c,2),round(d,2)]
print(new_list)