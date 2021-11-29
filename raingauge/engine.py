#engine.py
import sqlite3
import appconfig
import smtplib, ssl
from email.message import EmailMessage

class connection():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = conn.cursor()
        self.cache = None

     def execute(statement):
        self.c.execute(statement)
        self.cache = c.fetchall()
        return self.cache

    def read_cache():
        return [i for i in self.cache]

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
