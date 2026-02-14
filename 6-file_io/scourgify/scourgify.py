import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as infile, open(sys.argv[2], "w") as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            scourgify(reader, writer)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def scourgify(reader, writer):
    writer.writeheader()

    for row in reader:
        last, first = row["name"].split(",", 1)
        writer.writerow({
            "first": first.strip(),
            "last": last.strip(),
            "house": row["house"]
        })


main()
