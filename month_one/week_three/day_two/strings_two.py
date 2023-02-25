# Create a function that returns only strings with unique characters.
import sys

def function(string):
    
    for char in string:
        count = string.count(char)
        if count > 1:
            return "String is not unique"
        else:
            continue
    return string

print(function("hard"))
print(function("clever"))
     
            
            
            