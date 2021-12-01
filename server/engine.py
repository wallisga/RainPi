#engine.py
import sqlite3
import appconfig
import smtplib, ssl
from email.message import EmailMessage

class connection():

    def __init__(self):
        self.__db_connection = sqlite3.connect(appconfig.sql['name'])

    def __del__(self):
        self._disconnect()
 
    def _execute(self, statement, values=None):
        statements = ["SELECT * FROM "+ appconfig.sql['data'] +";", "INSERT INTO "+ appconfig.sql['data'] +" VALUES (:timestamp, :amount);"]
        cur = self.__db_connection.cursor()
        cur.execute(statements[statement])
        return [[i[0], i[1]] for i in cur.fetchall()]

    def _disconnect(self):
        self.__db_connection.close()

def startEmail(recp):
        msg = EmailMessage()
        msg.set_content("It has started to rain!")
        msg["Subject"] = "Rain Alert from RPi 4 Rain Gauge v0.1"
        msg["From"] = appconfig.alerting['source']
        msg["To"] = recp

        context = ssl.create_default_context()

        with smtplib.SMTP(appconfig.alerting['smtp'], port=587) as smtp:
                smtp.starttls(context=context)
                smtp.login(msg["From"], appconfig.alerting['password'])
                smtp.send_message(msg)

        return "Email sent to " + recp

def endEmail(recp):
        msg = EmailMessage()
        msg.set_content("Rain has not been detected for 30 minutes.")
        msg["Subject"] = "Rain Alert from RPi 4 Rain Gauge v0.1"
        msg["From"] = appconfig.alerting['source']
        msg["To"] = recp

        context = ssl.create_default_context()

        with smtplib.SMTP(appconfig.alerting['smtp'], port=587) as smtp:
                smtp.starttls(context=context)
                smtp.login(msg["From"], appconfig.alerting['password'])
                smtp.send_message(msg)

        return "Email sent to " + recp