FROM python:3.10-slim-buster

WORKDIR /FLASKPROJECT

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

WORKDIR /FLASKPROJECT/blueprintapp

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

WORKDIR /FLASKPROJECT

CMD ["python", "run.py"]