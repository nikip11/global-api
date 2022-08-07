FROM python:3.8.1-alpine

RUN apk upgrade --update --no-cache
RUN apk add --no-cache gcc g++ \
    tzdata \
    musl-dev linux-headers libffi-dev openssl-dev git libc-dev bash \
    mysql mysql-client postgresql-dev \
    libxml2 libxml2-dev libxslt-dev zlib-dev \
    ffmpeg jpeg-dev \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir psycopg2 \
    && pip install --no-cache-dir lxml \
    && pip install --no-cache-dir uwsgi \
    && pip install --no-cache-dir Pillow


COPY ./www/requirements.txt /www/requirements.txt
RUN pip install -r /www/requirements.txt

WORKDIR /www

# EXPOSE 5000
# CMD [ "flask", "run" ]
