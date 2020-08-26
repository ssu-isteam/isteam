#!/bin/bash

echo "[LOG] Cleaning up"
rm -r ~/isteam/*
pkill gunicorn

echo "[LOG] Setting up project"
cd ~/zips
unzip -q -o $(ls -t | head -n1) -d ~/isteam
cd ~/isteam

echo "[LOG] Setting up python env"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "[LOG] Building CSS"
npm i
npm run bundle -- --mode production

echo "[LOG] Starting up the application"
mv .prod.env .env
gunicorn isteam.wsgi:application --bind 0.0.0.0:8000 &
exit 0