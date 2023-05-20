FROM ubuntu:22.04
WORKDIR /app

RUN apt update && \
    apt install --no-install-recommends -y git python3 python3-dev python3-venv python3-pip python3-wheel build-essential  curl chromium-browser firefox -y && \
    pip install playwright pyppeteer  && \
    pyppeteer-install playwright install-deps playwright install chromium && \
    apt clean

COPY ./src .
RUN pip install -r requirements.txt
RUN chmod -R 777 /app
EXPOSE 8443 8080
CMD [ "python", "./bot.py" ]