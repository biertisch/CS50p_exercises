def main():
    camel = input("camelCase: ")
    print("snake_case:", snakefy(camel))


def snakefy(camel):
    snake = camel
    for c in snake:
        if c.isupper():
            snake = snake.replace(c, "_" + c.lower())

    return snake


main()
