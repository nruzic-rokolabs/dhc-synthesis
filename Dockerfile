FROM python:3.11

WORKDIR /service

COPY requirements.txt /service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /service/requirements.txt

COPY app /service/app
COPY settings.yml /service/

EXPOSE 8000

CMD ["fastapi", "run"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]