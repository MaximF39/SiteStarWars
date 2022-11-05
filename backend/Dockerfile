FROM python:3.10

COPY . /backend

WORKDIR /backend

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput
