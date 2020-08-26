#!/bin/bash

echo "[LOG] Cleaning up the directory"
rm -r ~/isteam/*

echo "[LOG] Setting up project"
cd ~/zips
unzip -q -o $(ls -t | head -n1) -d ~/isteam
cd ~/isteam

echo "[LOG] Setting up python env"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "[LOG] Build CSS"
npm i
npm run bundle -- --mode production