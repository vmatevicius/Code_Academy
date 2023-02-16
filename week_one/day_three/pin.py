pin = 4567

i = 0
while True:
    if i != pin:
        i += 1
    else:
        print("Pin code is:", pin)
        break
    