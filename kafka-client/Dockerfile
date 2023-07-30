FROM python:3.8-slim-buster

LABEL maintainer="Tomer Setty tsetty@outbrain.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

CMD ["python3", "Producer.py"]

