FROM python:3.10.0-slim

COPY . ./app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3000
CMD python entrypoint.py
