import random

def main():
    target = random.randint(1, get_n("Level: "))

    while True:
        guess = get_n("Guess: ")
        if guess == target:
            print("Just right!")
            return
        elif guess < target:
            print("Too small!")
        else:
            print("Too large!")


def get_n(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


main()
