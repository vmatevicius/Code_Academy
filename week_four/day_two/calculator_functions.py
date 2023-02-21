from typing import Optional

def divide(x: int | float, y: int | float) -> Optional[float]:
    
    try:
        return x / y
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")
        
def multiply(x: int | float, y: int | float) ->Optional[int | float]:

    try:
        return x * y
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")

def sum_up(x: int | float, y: int | float) -> Optional[int | float]: 

    try:
        return x + y
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")

def subtraction(x: int | float, y: int | float) -> Optional[int | float]:
    
    try:
        return x - y
    except ValueError:
        print("Wrong value")
    except TypeError:
        print("Wrong type")
    except Exception as e:
        print(f"Error : {e}")
