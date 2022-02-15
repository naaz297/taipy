# This is a simple Dockerfile to use while developing
# It's not suitable for production
#
# It allows you to run both flask and celery if you enabled it
# for flask: docker run --env-file=.flaskenv image flask run
# for celery: docker run --env-file=.flaskenv image celery worker -A myapi.celery_app:app
#
# note that celery will require a running broker and result backend
FROM python:3.9

RUN mkdir /code
WORKDIR /code

COPY Pipfile setup.py tox.ini ./
RUN pip install -U pip
RUN pip install pipenv
RUN pipenv install
# TODO Change taipy installation after publishing on pip
RUN pip install git+https://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@github.com/avaiga/taipy.git@v0.11.0#egg=taipy --pre
RUN pip install requests
RUN pip install -e .

COPY taipy_rest taipy_rest/
COPY migrations migrations/

EXPOSE 5000
