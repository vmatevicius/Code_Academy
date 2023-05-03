def get_valid_number(highest_number: int, input_text: str) -> int:
    while True:
        try:
            valid_numbers = []
            number = 0
            while number < highest_number:
                number += 1
                valid_numbers.append(number)
            user_input = int(input(input_text))
            if user_input in valid_numbers:
                return user_input
        except ValueError:
            print(f"You have to input numer between 1 and {highest_number}!")
            continue
