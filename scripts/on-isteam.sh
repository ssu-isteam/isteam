#!/bin/bash

echo "[LOG] Cleaning up"
rm -rf ~/isteam/*
pkill gunicorn

echo "[LOG] Setting up project"
cd ~/zips
unzip -q -o $(ls -t | head -n1) -d ~/isteam
cd ~/isteam

echo "[LOG] Setting up python env"
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
exec bash
poetry config virtualenvs.in-project true
poetry install
source .venv/bin/activate
./manage.py migrate groupware --settings isteam.settings.production
./manage.py migrate --settings isteam.settings.production

echo "[LOG] Building CSS"
npm i
npm run bundle -- --mode production

echo "[LOG] Collecting static file"
./manage.py collectstatic --noinput --settings isteam.settings.production

echo "[LOG] Starting up the application"
mv .prod.env .env
gunicorn isteam.wsgi:application --bind 0.0.0.0:8000 --daemon
