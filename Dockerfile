FROM tiangolo/uwsgi-nginx-flask:python3.6

# copy over our requirements.txt file
COPY home/ubuntu/flask_crypto_wallet/requirements.txt /tmp/
COPY etc/letsencrypt /etc/letsencrypt

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY /home/ubuntu/flask_crypto_wallet/app /app


