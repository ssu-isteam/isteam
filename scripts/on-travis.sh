#!/bin/bash

openssl aes-256-cbc -K $encrypted_f217180e22ee_key -iv $encrypted_f217180e22ee_iv -in id_rsa.enc -out id_rsa -d
openssl aes-256-cbc -K $encrypted_f182de71524d_key -iv $encrypted_f182de71524d_iv -in .prod.env.enc -out .prod.env -d

ssh -o StrictHostKeyChecking=no -i '../id_rsa' $SSH_HOST < scripts/on-isteam.sh