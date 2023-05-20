FROM python:3.11-slim-bullseye

RUN apt-get update && \
apt-get -y install chromium firefox-esr && \
  pip install -U pip && \
  pip install playwright && \
  playwright install && playwright install-deps && \
  pip install pyppeteer && \
  pyppeteer-install && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./src .
RUN pip install -r requirements.txt
CMD python3 bot.py
