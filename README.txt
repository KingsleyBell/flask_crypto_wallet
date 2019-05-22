# flask_crypto_wallet

sudo docker build -t crypto_wallet .
sudo docker run -d -v ~/tick.log:/app/tick.log -p 800:800 --env-file ./envfile -t crypto_wallet

