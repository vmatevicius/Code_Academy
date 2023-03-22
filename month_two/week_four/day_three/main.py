# write a function that accepts a number as a parameter.
# The function should return a number that’s the difference between the largest and smallest numbers that the digits can form in the number.
# For example, if the parameter is “213”, the function should return “198”, which is the result of 123 subtracted from 321.


# def get_difference(number: int, float) -> int:
#     if len(str(number)) == 1:
#         raise ValueError("Number must be atleast 2 digits long")
#     highest_number = "".join(sorted(str(number), reverse=True))
#     lowest_number = "".join(sorted(str(number)))
#     return int(highest_number) - int(lowest_number)

# write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.
# Values in the string can be separated by any number of zeros.
# The id is a numeric value but will contain no zeros.
# The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
# An example input would be “Robert000Smith000123”. The function should return the following using that input:
# { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

# from typing import Dict


# def decode_text(encoded_string: str) -> Dict[str]:
#     parts = encoded_string.split("0+")

#     first_name = parts[0]
#     last_name = parts[1]
#     id = parts[2]
#     return {"first_name": first_name, "last_name": last_name, "id": id}


# Write a function that returns dates of the 5 upcoming Friday 13ths, with Year, month and date

from datetime import datetime


def get_fridays_13th():
    pass
