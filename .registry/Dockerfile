FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.10 python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get install chromium-browser
RUN apt-get install firefox

WORKDIR /app
COPY ./src .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pyppeteer-install
EXPOSE 8443 8080
CMD [ "python", "./bot.py" ]