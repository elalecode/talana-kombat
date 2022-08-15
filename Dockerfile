FROM python:3.6.8-alpine

WORKDIR /code
RUN apk add --no-cache bash
RUN apk add postgresql-dev gcc python3-dev musl-dev build-base linux-headers pcre-dev
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code
