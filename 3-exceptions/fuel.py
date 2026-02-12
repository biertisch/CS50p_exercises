def main():
    n = get_fraction()
    print_percentage(n)


def get_fraction():
    while True:
        raw = input("Fraction: ")

        try:
            num, denom = raw.split("/", 1)
            x = int(num)
            y = int(denom)
            if (x < 0 or y < 1 or x > y):
                raise ValueError()
        except ValueError:
            pass
        else:
            return x / y


def print_percentage(n):
    if n >= 0.99:
        print("F")
    elif n <= 0.01:
        print("E")
    else:
        print(f"{round(n * 100)}%")


main()
