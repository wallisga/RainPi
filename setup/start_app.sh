#!/bin/sh
cd ../raingauge
./rainpienv/bin/activate
echo -e "from app import app\nif __name__ == '__main__':\n    app.run()" >> wsgi.py
gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app