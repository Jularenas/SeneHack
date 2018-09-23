import os
import hashlib
import math
import json
import ast

rootdir =os.path.dirname(os.path.abspath(__file__))+'/unificados.json'

def distance(origin, destination):
    lat1, lon1 = origin['latitud'],origin['longitud']
    lat2, lon2 = destination['latitud'],destination['longitud']
    radius = 6371 # km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def get10NearToRadius(location1,location2,radius1,radius2,users):
    nears=[]
    if users!=None:
        readJsonData(users,nears,location1,location2,radius1,radius2)
        print("After firebase",len(nears))
    if(len(nears)<10):
        with open(rootdir, 'r') as f:
            rutas = json.load(f)
            readJsonData(rutas,nears,location1,location2,radius1,radius2)
    return nears

def readJsonData(rutas,nears,location1,location2,radius1,radius2):
    for i in range(len(rutas)):
        if radius1>=distance(location1,rutas[i]['origen']):
            if radius2>=distance(location2,rutas[i]['destino']):
                nears.append(rutas[i])
                if len(nears)==10:
                    print('break')
                    break


