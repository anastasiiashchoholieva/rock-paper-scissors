FROM python:3.9.6-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PORT 5000


WORKDIR /app

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt


COPY . /app


EXPOSE $PORT


CMD ["python", "app.py"]
