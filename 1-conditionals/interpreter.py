def main():
    expr = input("Expression: ")
    a, op, b = expr.split()

    match op:
        case "+":
            print(float(a) + float(b))
        case "-":
            print(float(a) - float(b))
        case "*":
            print(float(a) * float(b))
        case "/":
            print(float(a) / float(b))


main()
