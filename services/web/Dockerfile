# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN  apt-get update && \
     apt-get install git -y

RUN git clone https://github.com/dkzhang/RMS.git #20200511-003

RUN pip install -r ./RMS/services/web/requirements.txt
