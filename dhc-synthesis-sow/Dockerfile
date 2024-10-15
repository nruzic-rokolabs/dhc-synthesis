FROM python:3.11

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./app /app

WORKDIR /app

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]
