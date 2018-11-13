FROM python:3.6-alpine

EXPOSE 8080
WORKDIR /app

COPY requirements.txt .
RUN apk update && \
    apk add --virtual .build-deps \
            musl-dev \
            linux-headers \
            gcc && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps && \
    rm -rf /var/cache/apk/*

COPY . .

CMD ["uwsgi", "--py-autoreload", "1", "--ini","uwsgi.ini"]
