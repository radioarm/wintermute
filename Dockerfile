FROM python:3.10

WORKDIR /srv

COPY ./requirements.txt /srv/requirements.txt
COPY ./.env /srv/.env

RUN pip install --no-cache-dir --upgrade -r /srv/requirements.txt

RUN python -m nltk.downloader all

COPY ./app /srv/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
