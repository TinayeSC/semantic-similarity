FROM python:3.7-slim

WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD python watch_next.py