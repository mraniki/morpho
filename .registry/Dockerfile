

FROM python:3.10

RUN apt-get update && \
  apt-get -y install libnss3 xvfb gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 \
  libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 \
  libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 \
  libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 \
  libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget && \
  rm -rf /var/lib/apt/lists/*

RUN pip install -U pip && pip install pyppeteer && pyppeteer-install
RUN pip install playwright && playwright install-deps && install chromium

WORKDIR /app
COPY ./src .
RUN pip install -r requirements.txt
CMD python3 bot.py



#UBNUTU
# FROM ubuntu:22.04
# WORKDIR /app

# RUN apt update && \
#     apt install --no-install-recommends -y git python3 python3-dev python3-venv python3-pip python3-wheel build-essential curl chromium-browser firefox -y && \
#     apt clean

# COPY ./src .
# # Add pptr user.
# RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
#     && mkdir -p /home/pptruser/Downloads \
#     && chown -R pptruser:pptruser /home/pptruser \
#     && chown -R pptruser:pptruser /app \
#     && chown -R pptruser:pptruser .
# # Run user as non privileged.

# RUN pip install pyppeteer
# RUN pyppeteer-install
# RUN pip install -r requirements.txt
# RUN playwright install-deps
# RUN playwright install chromium
# RUN chmod -R 777 /app
# USER pptruser
# EXPOSE 8443 8080
# CMD [ "python", "./bot.py" ]


#ALPINE
# FROM python:3-alpine

# RUN apk update
# RUN apk add py-pip
# RUN pip dynaconf fastapi uvicorn asyncio gspread pyppeteer playwright
# ENV LIBRARY_PATH=/lib:/usr/lib
# EXPOSE 8443 8080
# ADD . /app/
# WORKDIR /app/
# RUN python bot.py

