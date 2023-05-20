FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.10 python3-pip python3-wheel build-essential software-properties-common ca-certificates sudo tzdata wget curl firefox && add-apt-repository -y ppa:savoury1/chromium && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install chromium

WORKDIR /app
COPY ./src .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pyppeteer-install
EXPOSE 8443 8080
CMD [ "python", "./bot.py" ]