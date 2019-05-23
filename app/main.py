from flask import Flask, render_template

from auth import requires_auth

# the all-important app variable:
app = Flask(__name__)
# sslify = SSLify(app)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/wallet')
@requires_auth
def wallet():
    balances = []
    btc_balances = []
    zar_balances = []
    with open('tick.log', 'r') as wallet_file:
        for line in wallet_file:
            line = line.split('root:')[1]
            date = line.split('|')[0].split(' ')[0] + ' '
            amounts = line.split('|')[1:]
            btc_amount = float(amounts[0].split(' ')[-2])
            zar_amount = float(amounts[1].split(' ')[-1][1:-1])
            btc_balances.append([date, btc_amount])
            zar_balances.append([date, zar_amount])
            balances.append(' .  '.join([f'Date: {date}', f'BTC: {btc_amount}', f'ZAR: {zar_amount}']))

    return render_template(
        'wallet.html',
        balances=reversed(balances),
        btc_balances=btc_balances,
        zar_balances=zar_balances
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=800)
