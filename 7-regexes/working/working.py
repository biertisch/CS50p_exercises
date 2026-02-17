import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_pattern = r"\d\d?(?:\:\d\d)? (?:AM|PM)"
    pattern = rf"^({time_pattern}) to ({time_pattern})$"
    if matches := re.search(pattern, s.strip().lower(), re.IGNORECASE):
        try:
            first = validate_time(matches.group(1))
            second = validate_time(matches.group(2))
            return f"{first} to {second}"
        except ValueError as e:
            raise e
    else:
        raise ValueError("invalid pattern")


def validate_time(s):
    components = re.split(r"\W+", s)
    try:
        hours = int(components[0])
        if ":" in s:
            minutes = int(components[1])
            period = components[2]
        else:
            minutes = 0
            period = components[1]
    except TypeError:
        raise ValueError("Not integer")

    if not (1 <= hours <= 12) or not (0 <= minutes <= 59):
        raise ValueError("Invalid time value")

    if hours == 12 and period == "am":
        hours = 0
    elif hours != 12 and period == "pm":
        hours += 12

    return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
