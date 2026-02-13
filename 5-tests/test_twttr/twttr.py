def main():
    message = input("Input: ")
    print(f"Output: {shorten(message)}")


def shorten(word):
    for c in word:
        if is_vowel(c):
            word = word.replace(c, "")
    return word


def is_vowel(c):
    c = c.lower()
    return c == 'a'\
        or c == 'e'\
        or c == 'i'\
        or c == 'o'\
        or c == 'u'


if __name__ == "__main__":
    main()
