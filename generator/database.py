import paho.mqtt.client as paho
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["vasttrafik"]

broker="localhost"
port=1883

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("apicaller/data")

def on_message(client, userdata, msg):
	print("Message received:")
	print(str(msg.topic) + " " + str(msg.payload.decode()))

	message = msg.payload.decode()
	print(message)

	mycol = mydb["datapoints"]
	mydict = { "name": "John", "address": "Highway 37" }
	x = mycol.insert_one(mydict)
    
client = paho.Client()
client.connect(broker,port,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()