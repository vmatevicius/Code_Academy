# Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example.
from pyfiglet import Figlet
import random
from typing import Optional

figlet = Figlet()

fonts = figlet.getFonts()
    
def main(): 

    user_text = input("Say what's on your mind: ")
    
    print(transform_text(user_text))

def transform_text(text: str) -> Optional[str]:

    font_name = random.choice(fonts)
    figlet.setFont(font=font_name)
    try:
        changed_text = figlet.renderText(text)
    except TypeError:
        print("Wrong argument type")
    except Exception as e:
        print(f"Error : {e}")
    else:
        return changed_text
    finally:
        print("The try...except block is finished")
        
if __name__ == "__main__":
    main()