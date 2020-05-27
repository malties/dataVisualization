import requests
import paho.mqtt.client as paho
import json
import isodate
import threading
import caller
import organizer
import time
import datetime


threads=[]



broker = "test.mosquitto.org"
port = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("external")

def on_message(client, userdata, msg):
    time.sleep(1)
    print("Receiving message")
    message = msg.payload.decode()

    x= json.loads(message) # recieve the generated information from the generator

    orgLat= (x['origin']['latitude'])
    orgLong= (x['origin']['longitude'])
    desLat= (x['destination']['latitude'])
    desLong= (x['destination']['longitude'])
    

    try: #testing if value are of correct type
        originlat= float(orgLat) #checking if orgLat is actually a feasible number
        originLong= float(orgLong)
        destinationLat= float(desLat)
        destinationlong=float(desLong)
    except ValueError:
        print("the values recieved from the generator are not valid")
    
    else:
        #checking if the coordinates recieved are within the Gothenburg Area 
        if not 57.610 <= float(orgLat) <= 57.810 or not 11.723 <= float(orgLong) <= 12.157:
        #checkng if the coordinate values are within Gothenburg
            print("coordinates of origin are outside GB")
        elif not 57.610 <= float(desLat) <= 57.810 or not 11.723 <= float(desLong) <= 12.157:
            print("coordinates of destination are outside GB")
        else:
    
            thread= threading.Thread(target=on_thread, args=(x,))
            thread.start()
            threads.append(thread)


def on_thread(x):
    result=caller.call(x) # send coordinates to API 
    y=organizer.send_response(result) # handle the response back from the API
  
    client.publish("caller/points", json.dumps(y)) #publish the response to the visualiser
    

client = paho.Client()
client.connect(broker,port,60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
