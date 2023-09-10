#FROM python:3.11-slim-bullseye
FROM python:3.11-bookworm

RUN apt-get update && \
apt-get -y install chromium && \
  pip install -U pip && \
  pip install playwright && \
  playwright install && playwright install-deps && \
  rm -rf /var/lib/apt/lists/*

COPY . /app
RUN pip install --no-cache-dir /app
EXPOSE 8080

CMD [ "python", "/app/morpho/bot.py" ]
