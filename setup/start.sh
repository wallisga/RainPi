#!/bin/sh
cd ../server
./rainpienv/bin/activate
echo "from app import app\nif __name__ == '__main__':\n    app.run()" > wsgi.py
gunicorn3 -w 3 --bind 0.0.0.0:8000 --log-level=DEBUG wsgi:app