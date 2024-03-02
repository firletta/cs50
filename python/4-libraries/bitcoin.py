import sys
import json
import requests

try:
    num_bitcoins = float(sys.argv[1]) 
except IndexError:
    print('Error: Missing command-line argument')
    sys.exit(1)
except ValueError:
    print('Error: Command-line argument is not a number')
    sys.exit(1)

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = json.loads(response.text)
    bitcoin_price = data['bpi']['USD']['rate_float']
except requests.RequestException:
    print('Error fetching bitcoin price')
    sys.exit(1)

usd_value = bitcoin_price * num_bitcoins
print(f'${usd_value:,.4f}')