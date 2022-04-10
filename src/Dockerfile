FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/
COPY . /code/

RUN apk update && apk upgrade
RUN apk add --no-cache --update alpine-sdk linux-headers git zlib-dev openssl-dev gperf cmake
RUN pip3 install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/code/"
