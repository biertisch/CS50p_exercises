def main():
    fraction = get_fraction()
    percentage = convert(fraction)
    print(gauge(percentage))


def get_fraction():
    while True:
        fraction = input("Fraction: ")

        try:
            num, denom = fraction.split("/", 1)
            x = int(num)
            y = int(denom)
            if (x < 0 or y < 1 or x > y):
                raise ValueError()
        except ValueError:
            pass
        else:
            return fraction


def convert(fraction):
    num, denom = fraction.split("/", 1)

    x = int(num)
    y = int(denom)
    if y == 0:
        raise ZeroDivisionError()
    if (x < 0 or y < 0 or x > y):
        raise ValueError()

    return round(x / y * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
