FROM python:3.7-alpine
MAINTAINER Yusuf Can Bayrak <yusufcanbayrak@gmail.com>

# We copy just the requirements.txt first to leverage Docker cache
COPY ./Pipfile /app/Pipfile

WORKDIR /app

RUN pip3 install pipenv

COPY Pipfile ./

RUN pipenv lock
RUN pipenv install --deploy --system

COPY . .

ENV FLASK_ENV=production
ENV URL_PREFIX=api

RUN pytest .

EXPOSE 8000

HEALTHCHECK CMD python manage.py health_check

CMD [ "gunicorn", "-b", "0.0.0.0:8000", "evening.wsgi:app" ]
