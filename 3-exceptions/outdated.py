def main():
    while True:
        raw = input("Date: ")
        if convert_date(raw):
            break


def convert_date(raw):
    try:
        m, d, y = get_date(raw)
    except ValueError:
        return False

    print(f"{y:04}-{m:02}-{d:02}")

    return True


def get_date(raw):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    try:
        if "/" in raw:
            m, d, y = raw.split("/", 2)
        elif "," in raw:
            m_str, d, y = raw.replace(",", "").split(" ", 2)
            m = months.index(m_str) + 1
        else:
            raise ValueError()
    except ValueError:
        raise ValueError()

    return validate_values(m, d, y)


def validate_values(m, d, y):
    try:
        m = int(m)
        d = int(d)
        y = int(y)
    except ValueError:
        raise ValueError()

    if m < 1 or m > 12\
            or d < 1 or d > 31\
            or y < 0:
        raise ValueError()

    return m, d, y


main()
