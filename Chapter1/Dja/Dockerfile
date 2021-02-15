# Pull base image.
FROM python:3.8

# Set Environment variables.
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set work directory.
WORKDIR /code

# Install Depeendencies.
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/