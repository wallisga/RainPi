# save this as app.py
from flask import Flask
from engine import connection
import appconfig

app = Flask(__name__)

@app.route("/")
def landing():

    conn = connection(appconfig.sql['name'])
    data = conn.execute("SELECT * FROM "+ appconfig.sql['table'] +";")
    return "Sum of All Rainfall Recorded: " + str(sum(i[1] for i in data)/len(data)) + " mm of Rain"

if __name__=="__main__":
    app.run()