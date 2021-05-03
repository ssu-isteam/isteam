#!/bin/bash

chmod 711 ./scripts/local-init/*
./scripts/local-init/install-local-mysql.sh
./scripts/local-init/install-python-env.sh
cp .example.env .env
