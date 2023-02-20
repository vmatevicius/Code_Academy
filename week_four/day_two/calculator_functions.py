import sys

def divide(x: int | float, y: int | float) -> int | float:
    
    try:
        return x / y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")
        
def multiply(x: int | float, y: int | float) -> int | float:

    try:
        return x * y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")

def sum_up(x: int | float, y: int | float) -> int | float: 

    try:
        return x + y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")

def subtraction(x: int | float, y: int | float) -> int | float:
    
    try:
        return x - y
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
    except Exception as e:
        sys.exit(f"Error : {e}")
