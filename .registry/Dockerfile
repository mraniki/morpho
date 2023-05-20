FROM ubuntu:22.04
WORKDIR /app

RUN apt update && \
    apt install --no-install-recommends -y git python3 python3-dev python3-venv python3-pip python3-wheel build-essential curl chromium-browser firefox -y && \
    apt clean

COPY ./src .
# Add pptr user.
RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
    && mkdir -p /home/pptruser/Downloads \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /app \
    && chown -R pptruser:pptruser .
# Run user as non privileged.
USER pptruser
RUN pip install -r requirements.txt && \
    pyppeteer-install && \
    playwright install-deps && \
    playwright install chromium
RUN chmod -R 777 /app
EXPOSE 8443 8080
CMD [ "python", "./bot.py" ]