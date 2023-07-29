# syntax=docker/dockerfile:1
FROM python:3.10

WORKDIR /FruitShop/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# copy project
COPY . .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y make