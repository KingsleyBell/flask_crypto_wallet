from flask import Flask, render_template

# the all-important app variable:
app = Flask(__name__)



@app.route("/")
def hello():
    balances = []
    with open('/app/tick.log', 'r') as wallet_file:
        for line in wallet_file:
            balances.append(line)

    return render_template('wallet.html', balances=balances)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=800)
