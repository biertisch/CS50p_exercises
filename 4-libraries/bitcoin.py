import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        # update YourApiKey
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")
        r.raise_for_status()
        o = r.json()
    except requests.RequestException as e:
        sys.exit(f"HTTP request failed: {e}")

    try:
         price = float(o["data"]["priceUsd"])
    except ValueError:
        sys.exit("Conversion to float failed")

    print(f"${n * price:,.4f}")



main()
