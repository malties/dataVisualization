import isodate


def send_response(response):
    result= response[0]
    parameters= response[1] 
    requestId= response[2]
    stringID= str(requestId)
    
    showInJSON= result.json()

    new_payload = []
    temp = 0

   # in case there is no bus stops/ trips that satisfy the coordinates and time 
    if result.status_code== 500:
        print("unacceptable coordinates")
        
        new_payload=[]
         
        id= stringID
        originLat= parameters['originCoordLat']
        originLong= parameters['originCoordLong']
        destLat= parameters['destCoordLat']
        destLong= parameters['destCoordLong']
        date= parameters['date']
        time= parameters['time']
        print(originLat)
        print(id)

        weakOrigin={'lat': originLat, 'lng': originLong, 'time':time}
        weakDest= {'lat':destLat, 'lng': destLong}



        new_package1= {'Status': "failed",'id':id,'Origin': weakOrigin, 'Destination': weakDest}
        
        new_payload.append(new_package1)


    else:    

        trips= showInJSON['Trip']
        durations= []
        for trip in trips:
            trip_duration= trip['duration']
            yourdate= isodate.parse_duration(trip_duration)
            durations.append(yourdate)
        
        indix= durations.index(min(durations))
        chosenTrip= trips[indix]
        interested = chosenTrip['LegList']['Leg']
        
        
        # Creating new package that will be sent to the visualizer
        # The values get extracted from the fastest of the routes received from the API 

        for i in range(0,len(interested)):
            print("beggining of loop")
            

            id = stringID + "." + str(temp)
            name_origin = interested[i]['Origin']['name']
            type_origin = interested[i]['Origin']['type']
            lat_origin = interested[i]['Origin']['lat']
            lng_origin = interested[i]['Origin']['lon']
            time_origin= interested[i]['Origin']['time']
            


            new_origin = { 'name': name_origin, 'type': type_origin, 'lat': lat_origin, 'lng': lng_origin, 'time': time_origin }

            name_destination = interested[i]['Destination']['name']
            type_destination = interested[i]['Destination']['type']
            lat_destination = interested[i]['Destination']['lat']
            lng_destination = interested[i]['Destination']['lon']
            time_destination= interested[i]['Destination']['time']

            new_destination = { 'name': name_destination, 'type': type_destination, 'lat': lat_destination, 'lng': lng_destination, 'time': time_destination }

            new_package = { 'Status':'success','id': id, 'Origin': new_origin, 'Destination': new_destination}
            
            
            
            new_payload.append(new_package)
            temp += 1

        
        
    return new_payload
