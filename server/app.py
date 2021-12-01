# save this as app.py
from flask import Flask, request, jsonify, views
from engine import connection
import time
from auth import check_token

app = Flask(__name__)

@app.route("/")
def landing():
    return "WELCOME TO RAINPI"

@app.route("/rainfall/")
def get():
    if check_token(request.headers['X_KEY_X']):
        conn = connection()
        result = conn._execute(0)
        del conn
        return jsonify(result)
    else:
        return '', 400

@app.route("/rainfall/", methods=["POST"])
def post():
    if request.get_json()['timestamp'] < time.time() and isinstance(request.get_json()['amount'], float):
        conn = connection()
        result = conn._execute(1, request.get_json())
        del conn        
        return '', 204
    else:
        return '', 400