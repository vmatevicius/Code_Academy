import sys

def check_even_or_odd(number: int | float) -> str:
    
    try:
        if number % 2 == 0:
            return "even"
        return "odd"
    except TypeError:
        sys.exit("Argument must be an integer")
    except Exception as e:
        sys.exit(f"Error : {e}")