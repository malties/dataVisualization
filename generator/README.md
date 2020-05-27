**publisher.py**

Generates random two points in the area of Gothenburg and a time (in format hours:minutes) and after connecting to the MQTT Broker (Mosquitto) publishes this data. 
<br><br>

**GUI.py**

The same script as publisher with option of requests modification.
To be able to run the GUI you need to install pysimplegui. 
<br>
**pip3 install pysimplegui**
<br>
Run the scrpit by using the command python3 GUI.py to run the regular generator.
To configure the generator, use the command python3 GUI.py followed by a random argument.
ex:
**python3 GUI.py custom**
<br><br>

**subscriber.py**

Subscriber is a sample of what file that is uses mqtt mosquitto and subscribes to the content publishd by publisher.
It Connects to the MQTT Broker (Mosquitto) and subscribes to the same topic that the publisher is using to publish data. 
At every publication the data received is shown.
<br>
**!! This applicative (subscriber.py) is not going to be part of the generator, it is only used for testing purposes !!**

References: 
Steve Cope, Beginners Guide To The Paho MQTT Python Client, http://www.steves-internet-guide.com/into-mqtt-python-client/


