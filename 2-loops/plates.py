def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    for i in range(2):
        if not s[i].isalpha():
            return False

    n_found = False
    for c in s:
        if not c.isalnum():
            return False
        if c.isdigit() and not n_found:
            if c == '0':
                return False
            n_found = True
        if not c.isdigit() and n_found:
            return False

    return True


main()
