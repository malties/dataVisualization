**INTRODUCTION**

This project holds a component called ResRobot Caller. It contains three subcomponents, Communicator, Caller, and organizer.

**COMMUNICATOR**

The Communicator's main responsibility is to subscribe to the data published by the emitter.
The communicator also checks if the data recieved is valid in the context of our system and if it is, it forwards that data to
calller and organizer in a thread.
Using threads in this stage applies asynchronuousy. Thus, improving preformance. It is an appropriate place to introduce threads as 
the methods in the caller and organizer wait for external event
 Resources:
 https://realpython.com/intro-to-python-threading/
 
 http://www.steves-internet-guide.com/into-mqtt-python-client/
 
Required Libraries:
* import requests
* import paho.mqtt.client as paho
* import json
* import isodate
* import threading
* import caller
* import organizer
* import time
* import datetime

 
**CALLER**

The Caller's main responsibility is to call api ResRobot. Since there is a limit for the number of requests per minute,
the method is decorated by a circuit breaker, that raises an exception in the thread in case there is a failure response from the api 
the failure response is 400. The raised exception, stops the thread from proceeding to the Organizer.

Resources:
https://truveris.github.io/articles/pycon-2016/


Required Libraries: 
* import requests
* import json
* import isodate
* import pybreaker

**ORGANIZER**

The main Organizer's main responsibility is to iterate through the response from the api, extract the shortest trip from the 
list of responses.  When the response is 500, it means that there are no trips/bus stops that connect the coordinates published 
from the emitter. The method send_response method fowards a package that the Commuincator publishes it to the Visualizer.

Required Libraries:
* import isodate



