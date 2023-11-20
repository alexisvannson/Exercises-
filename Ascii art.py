import sys
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv)==1:
    text = input("Input: ")
    sys.exit(figlet.renderText(text))
elif len(sys.argv)>1 and (not sys.argv[1] in["-f","--font"] or  not sys.argv[-1] in figlet.getFonts()):
    print("Invalid usage")
    sys.exit(1)
else:
    text = input("Input: ")
    figlet.setFont(font=sys.argv[-1])
    print(figlet.renderText(text))
