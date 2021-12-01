# RainPi
RainPi is a client server application written in Python and designed to run on client Raspberry Pis. The RainPi clients monitor rainwater at a variety of locations and then report the rainwater detected in the area to the RainPi server. The RainPi clients transmit this data through an API model hosted on the RainPi server built with Flask, SQLite3, and Gunicorn. RainPi clients are designed to monitor rainwater with the Argent Weather Sensor Assembly p/n 80422 Imp Rain Gauge. Please see https://www.argentdata.com/files/80422_datasheet.pdf for the datasheet information.

# Guide
TBD

# To Do

Work in progress...reimagining the project as a multi-node solution. Client-server REST API data model will be implemented.

...need to implement a Bash script for WSGI setup - DONE

...need to implement API endpoints instead of simple web page - DONE

...need to implement API key feature - DONE

...need to clean up SQL to protect from injection - DONE

...need to implement client server model to RainPi so multiple Raspberry Pis can be provisioned in the field - IN PROGRESS

...reimagine data model for database to include multiple RainPi nodes - IN PROGRESS