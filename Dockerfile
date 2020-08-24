FROM python:3

WORKDIR /src

ENV DJANGO_SETTINGS_MODULE isteam.settings.production

COPY . /src/
RUN pip install -r requirements.txt