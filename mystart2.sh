python /home/site/wwwroot/manage.py
gunicorn --bind=0.0.0.0:$PORT app:app
