def get_field_value_type() -> str:
    type = input("Enter field value type(string, number(float, int)): ")
    if type in ["int", "float"]:
        if type == "int":
            min = int(input("Enter field min value(number): "))
            max = int(input("Enter field max value(number): "))
        if type == "float":
            min = float(input("Enter field min value(number): "))
            max = float(input("Enter field max value(number): "))
        return type, min, max
    else:
        return [type]


result = get_field_value_type()
print(result)
