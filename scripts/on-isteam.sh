#!/bin/bash

echo "[LOG] Cleaning up the directory"
cd ~/isteam
rm -r ./*

echo "[LOG] Setting up project"
unzip dist.zip
python3 -m venv venv

echo "[LOG] Setting up python env"
source venv/bin/activate
pip install -r requirements.txt

echo "[LOG] Build CSS"
npm i
npm bundle

