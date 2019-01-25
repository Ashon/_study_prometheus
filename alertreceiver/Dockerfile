FROM python:3.6

WORKDIR /opt/alertreceiver

RUN apt-get update \
    && apt-get install -y \
        libmemcached-dev \
        libldap2-dev \
    && apt-get clean

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src ./
COPY uwsgi.ini ./

EXPOSE 5000

CMD uwsgi -i uwsgi.ini
