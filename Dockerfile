FROM node:lts
WORKDIR /app
COPY . .
RUN npm i
RUN npm run bundle -- --mode production

FROM python:3.8
RUN pip install gunicorn
RUN pip install poetry

WORKDIR /app
COPY --from=0 /app/ .

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN ./manage.py migrate groupware --settings isteam.settings.production
RUN ./manage.py migrate --settings isteam.settings.production
# Static file 업로드
RUN ./manage.py collectstatic --noinput --settings isteam.settings.production
CMD gunicorn isteam.wsgi:application --bind 0.0.0.0:8000
