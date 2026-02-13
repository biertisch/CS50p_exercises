import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        score += play(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
        except ValueError:
            pass


def play(level):
    a = generate_integer(level)
    b = generate_integer(level)

    for _ in range(3):
        try:
            answer = int(input(f"{a} + {b} = "))
        except ValueError:
            print("EEE")
            continue

        if answer == a + b:
            return 1
        else:
             print("EEE")

    print(f"{a} + {b} = {a + b}")
    return 0


def generate_integer(level):
    if level < 0 or level > 3:
        raise ValueError()

    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
