from pyfiglet import Figlet
import random
from typing import Optional

figlet = Figlet()

fonts = figlet.getFonts()

def transform_text(text: str, font_name: str=None) -> Optional[str]:
    
    '''If font name is known, add second arg if not font will be random'''    
    
    if font_name:
        font_name = str(font_name)
    else:
        font_name = random.choice(fonts)
    figlet.setFont(font=font_name)
    try:
        changed_text = figlet.renderText(text)
    except TypeError:
        print("Wrong type of input")
    except Exception as e:
        print(f"Error : {e}")
    else:
        return changed_text
        