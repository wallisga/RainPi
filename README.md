# RainPi
RainPi is written in Python and designed to run on Raspberry Pi with SQLite3, Flask, and Gunicorn installed. RainPi is designed to monitor rainwater with the Argent Weather Sensor Assembly p/n 80422 Imp Rain Gauge. Please see https://www.argentdata.com/files/80422_datasheet.pdf for the datasheet information.

# Guide
TBD

# To Do

Work in progress...reimagining the project as a multi-node solution. Client-server REST API data model will be implemented.

...need to implement a Bash script for WSGI setup - DONE
...need to implement API endpoints instead of simple web page - DONE
...need to implement API key feature
...need to clean up SQL to protect from injection
...need to implement client server model to RainPi so multiple Raspberry Pis can be provisioned in the field
...reimagine data model for database to include multiple RainPi nodes