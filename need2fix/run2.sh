python manage.py collectstatic --noinput
python manage.py migrate --noinput
#python manage.py runserver 0.0.0.0:8000

exec  gunicorn --bind=0.0.0.0:80 need2fix.wsgi \
        --workers=5\
        --log-level=info \
        --log-file=-\
        --access-logfile=-\
        --error-logfile=-\
        --timeout 30000\
        --reload
