from typing import Optional

def str_compare(string_one: str, string_two: str) -> Optional[bool]:
    """Compare two strings, if equal return true else false"""

    try:
        if string_one == string_two:
            return True
        return False
    except Exception as e:
        print(f"Error : {e}")