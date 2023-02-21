from typing import Optional
def check_even_or_odd(number: int | float) -> Optional[str]:
    
    try:
        if number % 2 == 0:
            return "even"
        return "odd"
    except TypeError:
        print("Argument must be an integer")
    except Exception as e:
        print(f"Error : {e}")