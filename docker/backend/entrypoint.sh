
bash -c "python manage.py migrate --noinput
         && python manage.py collectstatic --noinput
         && gunicorn config.wsgi:application -c gunicorn.conf.py"

