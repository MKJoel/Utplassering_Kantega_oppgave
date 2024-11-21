FROM python:3

COPY ./src /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["fastapi", "run", "main.py"]


