import datetime
import sys
import re
import inflect


def main():
    s = input("Date of Birth: ").strip()
    try:
       print(minutes_since_birth(s))
    except Exception:
        sys.exit(f"Invalid date")


def minutes_since_birth(s):
    birth = get_date(s)
    delta = datetime.date.today() - birth
    minutes = round(delta.total_seconds() / 60)
    p = inflect.engine()
    s = f"{p.number_to_words(minutes)} minutes"
    return s.capitalize().replace(" and", "")


def get_date(s):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$", s):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        return datetime.date(year, month, day)
    else:
        raise ValueError()


if __name__ == "__main__":
    main()
