FROM python:3.6.5-slim-jessie
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/django-chartjs/src
ADD src/requirements.txt /usr/src/django-chartjs/src/
RUN pip install -r requirements.txt