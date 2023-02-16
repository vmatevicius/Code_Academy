# Create a pin code cracker. Let's say pin code consists of 4 random digits. You can store the value in variable.
# Then create a loop going through all possible combinations until you find the one you entered.

pin = 4567

i = 0
while True:
    if i != pin:
        i += 1
    else:
        print("Pin code is:", pin)
        break
    