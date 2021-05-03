#!/bin/bash

echo "[LOG] Setting up python env"
source .venv/bin/activate
./manage.py migrate groupware
./manage.py migrate

echo "[LOG] Building CSS"
npm i
npm run bundle

echo "[LOG] Collecting static file"
./manage.py collectstatic --noinput

echo "[LOG] starting up the application"
./manage.py runserver 0:8000
