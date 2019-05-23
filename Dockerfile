FROM tiangolo/uwsgi-nginx-flask:python3.6

# copy over our requirements.txt file
COPY requirements.txt /tmp/
COPY app/nginx.conf /etc/nginx/conf.d/nginx.conf
COPY data/letsencrypt /etc/letsencrypt

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./app /app


