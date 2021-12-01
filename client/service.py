#!/usr/bin/python3
#service.py
import RPi.GPIO as GPIO
import appconfig
import requests
import time

raining = False

# this many mm per bucket tip
CALIBRATION = 0.2794
# which GPIO pin the gauge is connected to
PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# variable to keep track of how much rain
rain = 0
rainstart = time.time()
# the call back function for each bucket tip
def cb(channel):
        global rain
        rain = rain + CALIBRATION

# register the call back for pin interrupts
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=cb, bouncetime=300)

# display and log results
while True:
        if rain > 0 and raining == False:
                raining = True
                rainstart = time.time()
                engine.startEmail(appconfig['destination'])
        elif rain == 0 and raining == True:
                if (time.time()-rainstart) > 360:
                        raining = False
                        engine.endEmail(appconfig['destination'])

        line = "%i, %f" % (time.time(), rain)
        print(line)
        ###This will be replaced with request to RainPi API and will require an API Key to authenticate.
        #db = engine.connection(appconfig.sql['name'])
        #db.execute(1, str(line))
        #db.conn.commit()
        #db.conn.close()
        #del db
        rain = 0
        time.sleep(60)

# close the log file and exit nicely
GPIO.cleanup()
