FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt upgrade -y && apt-get install --no-install-recommends -y python3.10 python3-pip python3-wheel build-essential software-properties-common ca-certificates chromium-browser firefox sudo && apt-get clean && rm -rf /var/lib/apt/lists/*

# create the ubuntu user
#RUN addgroup --gid 1000 ubuntu \
# && adduser --gecos "" \
#      --shell /bin/bash \
#      --uid 1000 \
#      --gid 1000 \
#      --disabled-password \
#      ubuntu \
# && adduser ubuntu adm

# make /var/log writeable by adm group
#RUN chgrp -R adm /var/log \
# && chmod -R g+w /var/log \
# && find /var/log -type d -exec chmod g+s {} #\;

# change to the ubuntu user
#USER root
#WORKDIR /home/ubuntu

# create common directories, some apps will fail if they don't exist
#RUN mkdir -p \
#  /home/ubuntu/.cache \
#  /home/ubuntu/.config \
#  /home/ubuntu/.local/share

WORKDIR /app
COPY --chmod=0755 ./src .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN pyppeteer-install
EXPOSE 8443 8080
CMD [ "python", "./bot.py" ]