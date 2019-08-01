from datetime import datetime
import logging
import requests

logging.getLogger("requests").setLevel(logging.WARNING)
logging.basicConfig(filename='/home/ubuntu/tick.log',level=logging.INFO)

binance_url = 'https://api.binance.com/api/v1/ticker/24hr'
# bittrex_vtc_price_url = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-vtc'
# bittrex_srn_price_url = 'https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-srn'
prices = requests.get(binance_url).json()
# vtc_price_result = requests.get(bittrex_vtc_price_url).json()
# srn_price_result = requests.get(bittrex_srn_price_url).json()


def get_coin_btc_price(symbol):
	return [coin for coin in prices if coin['symbol'] == symbol][0]['lastPrice']

ltc_price = get_coin_btc_price('LTCBTC')
eth_price = get_coin_btc_price('ETHBTC')
xmr_price = get_coin_btc_price('XMRBTC')
# vtc_price = get_coin_btc_price('VTC')
# vtc_price = vtc_price_result['result'][0]['Last']
# srn_price = srn_price_result['result'][0]['Last']
# omg_price = get_coin_btc_price('OMGBTC')
# xlm_price = get_coin_btc_price('XLMBTC')
# qsp_price = get_coin_btc_price('QSPBTC')
# trx_price = get_coin_btc_price('TRXBTC')
# req_price = get_coin_btc_price('REQBTC')
# etc_price = get_coin_btc_price('ETCBTC')

luno_ticker = requests.get('https://api.mybitx.com/api/1/ticker?pair=XBTZAR').json()
btc_price = (float(luno_ticker['bid']) + float(luno_ticker['ask'])) / 2

wallet = {
	'btc': {'amount': 0.18850968, 'btc_price': 1},
	'eth': {'amount': 9.08554372, 'btc_price': eth_price},
	'xmr': {'amount': 5.15612800, 'btc_price': xmr_price},
	'ltc': {'amount': 8.47162046, 'btc_price': ltc_price},
	# 'vtc': {'amount': 549.47223683, 'btc_price': vtc_price},
	# 'srn': {'amount': 2425.26654160, 'btc_price': srn_price},
	# 'omg': {'amount': 88.13293032, 'btc_price': omg_price},
	# 'xlm': {'amount': 1265.59200000, 'btc_price': xlm_price},
	# 'qsp': {'amount': 3711.04800000, 'btc_price': qsp_price},
	# 'trx': {'amount': 19402.57800000, 'btc_price': trx_price},
	# 'req': {'amount': 1579.41900000, 'btc_price': req_price},
	# 'etc': {'amount': 18.98100000, 'btc_price': etc_price}
}

total_btc = 0
for symbol, curr in wallet.items():
	curr_btc_total = curr['amount'] * float(curr['btc_price'])
	curr_rand_total = curr_btc_total * btc_price
	total_btc += curr_btc_total
	print(symbol, f'{curr_btc_total}BTC', f'R{curr_rand_total}')

total_btc_str = f'Total BTC: {round(total_btc, 4)}'
total_zar_str = f'Total rand: R{round(total_btc * btc_price, 2)}'
log_str = f'{datetime.now()} | {total_btc_str} | {total_zar_str}'

logging.info(log_str)

print(total_btc_str)
print(total_zar_str)
