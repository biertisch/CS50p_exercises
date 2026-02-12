def main():
    raw = input("Enter a string: ")
    proc = raw.replace(":)", "🙂").replace(":(", "🙁")
    print(proc)

main()