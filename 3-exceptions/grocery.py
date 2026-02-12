def main():
    items = {}

    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            print()
            break
        else:
            add_item(items, item)

    print_items(items)


def add_item(items, item):
    items[item] = items.get(item, 0) + 1


def print_items(items):
    for key in sorted(items):
        print(f"{items[key]} {key}")


main()
