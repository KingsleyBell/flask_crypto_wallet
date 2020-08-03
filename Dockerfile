FROM python:3.8-alpine
ADD ./app /app

COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]


