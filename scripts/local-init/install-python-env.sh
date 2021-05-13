#!/bin/bash

echo "[LOG] Install poetry"
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

echo "[LOG] Install python env"
poetry config virtualenvs.in-project true
poetry install
