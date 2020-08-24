FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /isteam

ADD . /isteam/
RUN pip install -r requirements.txt