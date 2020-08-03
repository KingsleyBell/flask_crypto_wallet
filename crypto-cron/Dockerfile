FROM python:3.8-alpine

ADD ./tick.py /cron/tick.py
COPY requirements.txt /cron/requirements.txt

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /cron/requirements.txt

WORKDIR /cron
CMD ["python", "tick.py"]
