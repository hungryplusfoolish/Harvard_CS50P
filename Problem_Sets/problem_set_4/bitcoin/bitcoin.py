import json
import sys
import requests

def main():
    try:
        coin_desk = json.dumps(requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json(), indent = 2)
        coin_desk = json.loads(coin_desk)

        btc_price = float(coin_desk.get("bpi",{}).get("USD",{}).get("rate_float"))
        try:
            if len(sys.argv) == 2:
                quantity = float(sys.argv[1])
                cost =  btc_price * quantity
                cost = "{:,.4f}".format(cost)
                print("$"+str(cost))

            else:
                sys.exit("Command-line arguement is not a number")

        except ValueError:
            sys.exit("Command-line arguement is not a number")

    except requests.RequestException:
        sys.exit("Request error")

if __name__ == "__main__":
    main()
