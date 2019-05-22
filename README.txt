# flask_crypto_wallet

# build from /
sudo docker build -t crypto_wallet .
sudo docker run -d -v ~/tick.log:/app/tick.log -p 80:80 --env-file ./envfile -t crypto_wallet

