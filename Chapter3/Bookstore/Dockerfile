# Pull base image.
FROM python:3.8

# Set Environment Variable.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

RUN mkdir -p /deploy/logs
RUN touch /deploy/logs/error.log
RUN touch /deploy/logs/access.log

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/