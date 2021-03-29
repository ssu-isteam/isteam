FROM python:3.8

COPY . /app/
WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN $HOME/.poetry/bin/poetry config virtualenvs.in-project true
RUN $HOME/.poetry/bin/poetry install
RUN .venv/bin/python manage.py migrate
RUN $HOME/.poetry/bin/poetry build
CMD [".venv/bin/python", "manage.py", "runserver", "0.0.0.0:80"]