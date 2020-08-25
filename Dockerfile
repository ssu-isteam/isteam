FROM python:3

WORKDIR /src

ENV DJANGO_SETTINGS_MODULE isteam.settings.production
ENV PYTHONUNBUFFERED 1

COPY . /src/
RUN pip install -r requirements.txt

# Installing Node.js
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN npm install
RUN npm run bundle