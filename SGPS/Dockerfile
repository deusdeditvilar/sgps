FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install -r requirements.txt && \
        python manage.py makemigrations --settings=SGPS.settings.prod && \
        python manage.py migrate --settings=SGPS.settings.prod
