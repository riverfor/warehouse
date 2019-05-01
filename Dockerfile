FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-docker
WORKDIR /django-docker
ADD requiments.txt /django-docker/
RUN pip install -r requiments.txt
ADD . /django-docker/

