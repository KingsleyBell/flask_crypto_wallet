from datetime import datetime
import requests

base_url = 'https://min-api.cryptocompare.com/data/histoday'
end_date = datetime(2018,8,3)
end_ts = int(end_date.strftime('%s'))
days_back = 750
btc_balance = 0.18850968

WALLET = {
	'eth': 9.08554372,
	'xmr': 5.15612800,
	'ltc': 8.47162046
}

params = {
    'fsym': 'BTC',
    'tsym': 'BTC',
    'limit': days_back,
    'toTs': end_ts
}

history = {}


# Get btc prices for other currencies
for currency, amount in WALLET.items():
    params['fsym'] = currency.upper()
    response = requests.get(base_url, params=params).json()
    data = response['Data']
    for snapshot in data:
        ts = snapshot['time']
        if ts not in history:
            history[ts] = {}

        history[ts][currency] = snapshot['open'] * amount

params['fsym'] = 'BTC'
params['tsym'] = 'ZAR'
btc_history = requests.get(base_url, params=params).json()['Data']

# get total btc and zar per history instance
for ts, balances in history.items():
    btc_total = btc_balance
    for currency in WALLET.keys():
        btc_total += balances[currency]

    balances['btc'] = btc_total
    btc_zar = [balance for balance in btc_history if balance['time'] == ts][0]['open']
    balances['zar'] = round(btc_zar * btc_total, 2)

# output
out_file = open('/Users/luke/Downloads/restro_wallet.txt', 'w')
for ts, balances in history.items():
    date_string =  datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')
    line = f'INFO:root:{date_string} | Total BTC: {balances["btc"]} | Total rand: R{balances["zar"]}\n'
    out_file.write(line)
