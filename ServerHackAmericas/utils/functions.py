import os
import hashlib
import math
import json

rootdir ='C:/Users/rtb15/Desktop/HackAmericas/SeneHack/ServerHackAmericas/utils/unificados.json'

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