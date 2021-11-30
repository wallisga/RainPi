# save this as app.py
from flask import Flask, request, jsonify
from engine import connection
import time

app = Flask(__name__)

@app.route("/")
def landing():
    return "WELCOME TO RAINPI"

@app.route("/rainfall")
def get():
    conn = connection()
    result = conn._execute(0)
    del conn
    return jsonify(result)

@app.route("/rainfall", methods=["POST"])
def post():
    print(request.get_json()['timestamp'] > time.time())
    if request.get_json()['timestamp'] < time.time() and isinstance(request.get_json()['amount'], float):
        conn = connection()
        result = conn._execute(1, request.get_json())
        del conn        
        return '', 204
    else:
        return '', 400

if __name__=="__main__":
    app.run()