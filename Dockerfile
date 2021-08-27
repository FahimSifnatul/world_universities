FROM python:3.8-slim-buster
WORKDIR /world_universities
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic