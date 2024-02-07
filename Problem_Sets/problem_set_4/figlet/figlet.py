import sys
import random
from pyfiglet import Figlet

#variables
length_argv = len(list(sys.argv))
figlet = Figlet()
fonts = figlet.getFonts()

#inputs

if length_argv == 3:
    file = sys.argv[1]
    style = sys.argv[2]
    
    if file in ["-f","--f"] and style in fonts:
        string = input("Input: ")
        print("Output: \n",Figlet(font = style).renderText(string))
    
    else:
        print("Invalid usage")
        sys.exit()

elif length_argv == 1:
    string = input("Input: ")
    print("Output: \n",Figlet(font = random.choice(fonts)).renderText(string))

else:
    sys.exit()