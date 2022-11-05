bash -c "gunicorn config.wsgi:application -c ./config/gunicorn.conf.py"

