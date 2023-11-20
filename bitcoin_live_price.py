import requests
import sys
import json
try:
    amount = float(sys.argv[1])
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    sorted_data = data.json()
    #sorted_data1 = json.dumps(data.json(), indent=2)
    bitcoin_price = float(sorted_data["bpi"]["USD"]["rate"].replace(',', ''))
except IndexError:
  sys.exit("Missing command-line argument")
except ValueError:
   sys.exit("Command-line argument is not a number")
except requests.RequestException:
   sys.exit("requests.RequestException")
else:
   print(f"${'{:,.4f}'.format(round(amount * bitcoin_price,4))}")
   sys.exit(0)
