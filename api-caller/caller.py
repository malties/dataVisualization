import requests
import json
import isodate
import pybreaker


#the breaker sets the parameters for which the circuit breaker follows
#two consecutive fails and the circuit breaker opens 
#it waits for 15 seconds until it closes again 
breaker = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=15) 
    

#decorate this method with circuit breaker
@breaker
def call(x):

    origin= (x['origin'])
    requestId=(x['requestId'])
    originLat= (origin['latitude'])
    originLong= (origin['longitude'])
    destination=(x['destination'])
    destinationLat= (destination['latitude'])
    destinationLong= (destination['longitude'])

    timeOfDeparture= (x['timeOfDeparture'])

    time= timeOfDeparture.split(" ")

    date= time[0]
    departureTime= time[1]
    

    parameters= {
        "originCoordLat":originLat,
        "originCoordLong":originLong,
        "destCoordLat":destinationLat,
        "destCoordLong":destinationLong,
        "date": date,
        "time": departureTime,
        "format": "json"
    }

    url = "https://api.resrobot.se/v2/trip?key=343406ee-99cc-45f9-b07c-c4d1a61a9107"
    
    
    response = requests.get(url, params=parameters, timeout=3)
    print(response.status_code)
    if(response.status_code==400): #when error is 400, circuit breaker opens
        raise pybreaker.CircuitBreakerError

    
    print("HERE")


    return response, parameters, requestId
