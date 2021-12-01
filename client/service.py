#!/usr/bin/python3
#service.py
import RPi.GPIO as GPIO
import piconfig
import requests
import time
import json

#Initial variables
raining = False
headers=piconfig['key']
headers['Content-Type'] = 'application/json'
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
        elif rain == 0 and raining == True:
                if (time.time()-rainstart) > 360:
                        raining = False
        #The third parameter should be replaced with pi_id. For now it is 1.
        line = "%i, %f, %i" % (time.time(), rain, 1)
        print(line)
        response = requests.request("POST", piconfig['url'], headers=headers, payload=json.dumps({'timestamp': time.time(), 'amount': rain, 'pi_id': piconfig['pi_id']}))
        if response.status_code != 204:
                print(response.status_code)
                print(response.text)      
        rain = 0
        time.sleep(60)

# close the log file and exit nicely
GPIO.cleanup()
