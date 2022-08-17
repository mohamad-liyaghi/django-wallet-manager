FROM python:latest

WORKDIR /code

COPY requirement.txt /code/
RUN pip install -r requirement.txt

COPY . /source/