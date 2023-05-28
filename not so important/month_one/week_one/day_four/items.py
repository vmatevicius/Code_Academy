# print all the items separated with "|"

items = ["a_string", 5, 5.5, (5, 10), [6, 8], {"Key": "value",}, True]

for i in items:
    print(f" {i} ", end="|")
print()