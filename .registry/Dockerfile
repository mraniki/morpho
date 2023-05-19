FROM ubuntu:latest

RUN apt-get update; apt-get clean

# Install wget.
RUN apt-get install -y wget

RUN apt-get install -y gnupg

# Set the Chrome repo.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Install Chrome.
RUN apt-get update && apt-get -y install google-chrome-stable
RUN apt-get -y install firefox


WORKDIR /app
COPY ./src .
# COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8443 8080
CMD [ "python", "./bot.py" ]