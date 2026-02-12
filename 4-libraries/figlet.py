import sys
import random
import pyfiglet

def main():
    f = pyfiglet.Figlet()
    fonts = f.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3:
        if (sys.argv[1] != "-f" and sys.argv[1] != "--font")\
            or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    message = input("Input: ")
    print("Output:")
    print(pyfiglet.figlet_format(message, font=font))


main()
