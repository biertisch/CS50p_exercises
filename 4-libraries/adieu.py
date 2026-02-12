import inflect

def main():
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(names)}")


main()
