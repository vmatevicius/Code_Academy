roman_values = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


class Converter:
    @staticmethod
    def convert_to_roman(number: int) -> str:
        roman_number = []
        counter = 0
        while counter != number:
            for key, value in roman_values.items():
                if number == value:
                    return key


print(Converter().convert_to_roman(900))
