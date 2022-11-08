FROM python:3.10

COPY . /backend

WORKDIR /backend

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

ENTRYPOINT python manage.py migrate --noinput && gunicorn config.wsgi:application -c config/gunicorn.conf.py
