# save this as app.py
from flask import Flask
from engine import connection
import appconfig

app = Flask(__name__)

@app.route("/")
def landing():

    conn = engine.connection(appconfig.sql['name'])
    data = conn.execute("SELECT * FROM "+ appconfig.sql['table'] +";")
    data = []
    for i in range(-6,-1):
        amount+=data[i][1]
    return "Rainfall in Last Five Minutes: " + str(amount) + " mm of Rain"

if __name__=="__main__":
    app.run()
