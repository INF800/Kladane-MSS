FROM python:3.7.5

EXPOSE 80

COPY . /app

RUN pip install -r requirements.txt