FROM python:3

WORKDIR /src

ENV DJANGO_SETTINGS_MODULE isteam.settings.production
ENV PYTHONUNBUFFERED 1

COPY . /src/
RUN pip install -r requirements.txt