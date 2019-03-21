FROM tnir/mysqlclient

MAINTAINER WHuangz Dev

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SE_ENV_NAME="development"


COPY ./requirements.txt app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app
COPY ./app /app
