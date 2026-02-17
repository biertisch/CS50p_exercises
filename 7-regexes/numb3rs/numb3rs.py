import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    if matches := re.search(pattern, ip.strip()):
       for group in matches.groups():
           if not validate_group(group):
                return False
    else:
        return False
    return True


def validate_group(group):
    if group.startswith("0") and len(group) > 1:
        return False
    try:
        n = int(group)
    except TypeError:
        return False
    return 0 <= n <= 255


if __name__ == "__main__":
    main()
