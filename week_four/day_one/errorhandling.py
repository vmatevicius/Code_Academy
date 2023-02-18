# Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example.
from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

fonts = figlet.getFonts()
    
def main(): 

    user_text = input("Say what's on your mind: ")
    
    print(transform_text(user_text))

def transform_text(text):

    font_name = random.choice(fonts)
    figlet.setFont(font=font_name)
    try:
        changed_text = figlet.renderText(text)
    except TypeError:
        sys.exit("Wrong type of input")
    else:
        return changed_text
    finally:
        print("The try...except block is finished")
        
if __name__ == "__main__":
    main()