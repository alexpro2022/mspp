FROM python:3.11-slim

WORKDIR /app

COPY /requirements .

RUN python -m pip install --upgrade pip
RUN pip install -r /requirements/development.txt

COPY ./src .

CMD ["uvicorn ", "config.asgi:application"]
