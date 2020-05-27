import sys
import PySimpleGUI as sg
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

client = paho.Client()
client.on_publish = on_publish

fake = Faker()

requests_per_minute = 30

deviceId = fake.pyint(min_value=0, max_value=9999, step=1)

if len(sys.argv) == 2:
    sg.change_look_and_feel('DarkAmber')  # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...

    column1 = [[sg.Radio('Choose time', 'radio3')],
               [sg.InputText("mm", size=(4, 1)), sg.InputText("dd", size=(4, 1))],
               [sg.InputText("h", size=(4, 1)), sg.InputText("min", size=(4, 1))]]

    layout = [[sg.Text('Please enter borker')],
              [sg.InputText('test.mosquitto.org')],
              [sg.Text('Choose port')],
              [sg.InputText(1883)],
              [sg.Text('Choose one of the popular origins'), sg.Radio('random', 'radio1', default=True),
               sg.Radio('stadium', 'radio1')],
              [sg.Text('Choose one of the popular destination'), sg.Radio('random', 'radio2', default=True),
               sg.Radio('Lindholmspiren', 'radio2')],
              [sg.Radio('Use Current Time', 'radio3'), sg.Column(column1)],
              [sg.OK(), sg.Cancel()]]

    # Create the Window
    window = sg.Window('Configure data generator', layout)
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        print(values)
        broker = values[0];
        port = int(values[1]);
        client.connect(broker, port, 60)

        gbLat = 57.710  # latitude of the center of the city of gothenburg
        gbLng = 11.973  # longitude of the center of the city of gothenburg
        currentTime = datetime.datetime.now()
        startTime = datetime.datetime.now()
        prevTime = 0

        i = 0

        while True:
            if values[6] & int((datetime.datetime.now() - startTime).total_seconds()) > prevTime:
                prevTime = int((datetime.datetime.now() - startTime).total_seconds())
                currentTime += datetime.timedelta(minutes=1)

            requestId = i
            i += 1

            epoch = time.time()
            if not values[2]:
                latA = 57.7072
                lngA = 11.9668
            else:
                latA = str(fake.coordinate(center=gbLat, radius=0.10))
                lngA = str(fake.coordinate(center=gbLng, radius=0.15))

            if not values[4]:
                latB = 57.7055
                lngB = 11.9399
            else:
                latB = str(fake.coordinate(center=gbLat, radius=0.10))
                lngB = str(fake.coordinate(center=gbLng, radius=0.15))

            if values[7]:
                ts = "2020-" + values[8] + "-" + values[9] + " " + values[10] + ":" + values[11]

            else:
                ts = currentTime.strftime("%Y-%m-%d %H:%M")

            if fake.pyint(min_value=0, max_value=1, step=1) == 0:
                purpose = "work"
            else:
                purpose = "leisure"

            json_data = {
                'deviceId': deviceId,
                'requestId': requestId,
                'origin': {
                    'latitude': latA,
                    'longitude': lngA
                },
                'destination': {
                    'latitude': latB,
                    'longitude': lngB
                },
                'timeOfDeparture': ts,
                'purpose': purpose,
                'issuance': epoch
            }

            print(json.dumps(json_data, indent=4, sort_keys=True))

            time.sleep(60 / requests_per_minute)
            client.publish("external", json.dumps(json_data))

        # hour = currentTime.hour
        # if (hour >= 7 and hour < 9) or (hour >= 15 and hour < 18):
        #	sleepTime = 0.1
        # else:
        #	sleepTime = 1

        # time.sleep(sleepTime)

        client.disconnect()

        if event in (None, 'Cancel'):
            break
else:
    broker = "test.mosquitto.org"
    port = 1883
    client.connect(broker, port, 60)
    gbLat = 57.710  # latitude of the center of the city of gothenburg
    gbLng = 11.973  # longitude of the center of the city of gothenburg
    currentTime = datetime.datetime.now()
    startTime = datetime.datetime.now()
    prevTime = 0
    i = 0
    while True:
        if int((datetime.datetime.now() - startTime).total_seconds()) > prevTime:
            prevTime = int((datetime.datetime.now() - startTime).total_seconds())
            currentTime += datetime.timedelta(minutes=1)

        requestId = i
        i += 1

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
            'origin': {
                'latitude': latA,
                'longitude': lngA
            },
            'destination': {
                'latitude': latB,
                'longitude': lngB
            },
            'timeOfDeparture': ts,
            'purpose': purpose,
            'issuance': epoch
        }

        print(json.dumps(json_data, indent=4, sort_keys=True))

        time.sleep(60 / requests_per_minute)
        client.publish("external", json.dumps(json_data))

    # hour = currentTime.hour
    # if (hour >= 7 and hour < 9) or (hour >= 15 and hour < 18):
    #	sleepTime = 0.1
    # else:
    #	sleepTime = 1

    # time.sleep(sleepTime)

    client.disconnect()


