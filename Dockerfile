FROM python:3.11

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY .env ..
COPY src/ .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:create_app()"]
