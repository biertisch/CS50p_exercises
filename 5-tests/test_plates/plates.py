def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # lenght between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # start with at least 2 letters
    for i in range(2):
        if not s[i].isalpha():
            return False

    n_found = False;
    for c in s:
        # only letters and numbers allowed
        if not c.isalnum():
            return False

        # numbers allowed only at end
        if c.isdigit() and not n_found:
            if c == '0':
                return False
            n_found = True
        if not c.isdigit() and n_found:
            return False

    return True


if __name__ == "__main__":
    main()
