def main():
    message = input("Input: ")

    for c in message:
        if is_vowel(c):
            message = message.replace(c, "")

    print("Output:", message)


def is_vowel(c):
    c = c.lower()
    return c == 'a'\
        or c == 'e'\
        or c == 'i'\
        or c == 'o'\
        or c == 'u'


main()