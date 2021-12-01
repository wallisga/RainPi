from flask import Flask, request, jsonify, views
from engine import connection
import time
from auth import check_token

app = Flask(__name__)

@app.route("/")
def landing():
    return "WELCOME TO RAINPI"

@app.route("/rainfall/")
def get_rainfall():
    try:
        if check_token(request.headers['X_KEY_X']):
            conn = connection()
            result = conn._execute(0)
            del conn
            return jsonify(result)
        else:
            return 'Invalid key', 401
    except KeyError as e:
        return 'Key not provided', 400

@app.route("/rainfall/", methods=["POST"])
def add_rainfall():
    try:
        if check_token(request.headers['X_KEY_X']):
            if isinstance(request.get_json()['timestamp'], int) and isinstance(request.get_json()['amount'], float):
                conn = connection()
                result = conn._execute(1, request.get_json())
                del conn        
                return '', 204
            else:
                return 'Bad payload', 400
        else:
            return 'Invalid key', 401
    except KeyError as e:
        print(e)
        return 'Key not provided', 400