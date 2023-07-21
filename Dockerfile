FROM python:3.10.5-slim

RUN apt-get update && apt-get install -y gettext && apt clean && rm -rf /var/cache/apt/*
RUN pip install --upgrade pip

COPY ./requirements.txt /tmp/


#================================================
# PIP packages
#================================================
RUN pip install --no-cache-dir -r /tmp/requirements.txt


#================================================
# Code
#================================================
RUN useradd -m -d /proj -s /bin/bash app
COPY . /proj
WORKDIR /proj/project
USER app
