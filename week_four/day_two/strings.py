import sys

def str_compare(string_one: str, string_two: str) -> bool:

    try:
        if string_one == string_two:
            return True
        return False
    except Exception as e:
        sys.exit(f"Error : {e}")