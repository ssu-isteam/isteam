#!/bin/bash

openssl aes-256-cbc -K $encrypted_f182de71524d_key -iv $encrypted_f182de71524d_iv -in .prod.env.enc -out .prod.env -d

sudo apt update
sudo apt install sshpass

filename=$(date '+%Y-%m-%d')

zip -r "${filename}.zip" .

echo "[LOG] Uploading .zip file"
sshpass -p "$SSH_PASS" scp ${filename}.zip $SSH_HOST:~/zips
echo "[LOG] Connecting ssh"
sshpass -p "$SSH_PASS" ssh -o StrictHostKeyChecking=no $SSH_HOST < scripts/on-isteam.sh