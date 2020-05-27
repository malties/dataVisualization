import paho.mqtt.client as paho
from faker import Faker
import json
import datetime
import time

def on_publish(client,userdata,result):
    print("data published \n")
    print("userdata: " + str(userdata))
    print("result: " + str(result))
    pass

fake = Faker()

requests_per_minute = 30

broker="test.mosquitto.org"
port=1883

deviceId = fake.pyint(min_value=0, max_value=9999, step=1)

# the coordinates are generated in the area of gothenburg

gbLat = 57.710	# latitude of the center of the city of gothenburg
gbLng = 11.973	# longitude of the center of the city of gothenburg

# RUSH HOURS 7 to 9, 15 to 18
client = paho.Client()
client.on_publish = on_publish
client.connect(broker,port,60)

currentTime = datetime.datetime.now()

startTime = datetime.datetime.now()
prevTime = 0

i=0

while True:
	if int((datetime.datetime.now() - startTime).total_seconds()) > prevTime:
		prevTime = int((datetime.datetime.now() - startTime).total_seconds())
		currentTime += datetime.timedelta(minutes=1)

	requestId = i
	i+=1

	epoch = time.time()

	latA = str(fake.coordinate(center=gbLat, radius=0.10))
	lngA = str(fake.coordinate(center=gbLng, radius=0.15))
	latB = str(fake.coordinate(center=gbLat, radius=0.10))
	lngB = str(fake.coordinate(center=gbLng, radius=0.15))

	ts = currentTime.strftime("%Y-%m-%d %H:%M")

	if fake.pyint(min_value=0, max_value=1, step=1) == 0:
		purpose = "work"
	else:
		purpose = "leisure"

	json_data = {
		'deviceId': deviceId,
		'requestId': requestId,
		'origin':{
			'latitude': latA,
			'longitude': lngA
		},
		'destination':{
			'latitude': latB,
			'longitude': lngB
		},
		'timeOfDeparture': ts,
		'purpose': purpose,
		'issuance' : epoch
	}

	print(json.dumps(json_data, indent=4, sort_keys=True))

	time.sleep(60/requests_per_minute)
	client.publish("external", json.dumps(json_data))

	#hour = currentTime.hour
	#if (hour >= 7 and hour < 9) or (hour >= 15 and hour < 18):
	#	sleepTime = 0.1
	#else:
	#	sleepTime = 1

	#time.sleep(sleepTime)

client.disconnect()
