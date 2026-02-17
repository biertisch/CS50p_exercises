import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(?:\b|\W)um(?:\b|\W)"
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
