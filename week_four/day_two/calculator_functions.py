import sys

def divide(x, y):
    
    try:
        return round(float(x) / float(y), 2)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")
        
def multiply(x, y):

    try:
        return round(float(x) * float(y), 2)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")

def sum_up(x, y):

    try:
        return round(float(x) + float(y), 1)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")

def subtraction(x, y):
    
    try:
        return round(float(x) - float(y), 1)
    except ValueError:
        sys.exit("Wrong value")
    except TypeError:
        sys.exit("Wrong type")