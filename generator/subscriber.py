import paho.mqtt.client as paho
broker="localhost"
port=1883

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("generator/points")

def on_message(client, userdata, msg):
    print("Message received:")
    print(str(msg.topic) + " " + str(msg.payload.decode()))
    
    message = msg.payload.decode()
    divided = message.split(",")
    print(divided[0] + " " + divided[1] + " " + divided[2] + " " + divided[3])
    print(divided[4])
    
client = paho.Client()
client.connect(broker,port,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()