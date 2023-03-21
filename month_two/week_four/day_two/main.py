# write a python script that adds all the numbers entered in the command line as arguments.
# Throw an error if user enters something other than number
import sys

try:
    numbers = [int(number) for number in sys.argv[1:]]
    print(sum(numbers))
except ValueError:
    sys.exit("Arguments must be numbers")
