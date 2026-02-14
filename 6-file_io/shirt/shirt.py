import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not valid_format(sys.argv[1]):
        sys.exit("Invalid input")
    if not valid_format(sys.argv[2]):
        sys.exit("Invalid output")
    if not same_extension(sys.argv[1], sys.argv[2]):
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1]) as student, Image.open("shirt.png") as shirt:
            student = ImageOps.fit(student, size=shirt.size)
            student.paste(shirt, shirt)
            student.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exit")


def valid_format(s):
    return s.strip().lower().endswith(".jpg")\
        or s.strip().lower().endswith(".jpeg")\
        or s.strip().lower().endswith(".png")


def same_extension(s1, s2):
    if s1.strip().lower().endswith(".jpg"):
        extension = ".jpg"
    elif s1.strip().lower().endswith(".jpeg"):
        extension = ".jpeg"
    else:
        extension = ".png"

    return s2.strip().lower().endswith(extension)


main()