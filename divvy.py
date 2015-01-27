import json
from urllib.request import urlopen\



webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)


ide = result['stationBeanList'][276]['id']
nam = result['stationBeanList'][276]['stationName']
ava = result['stationBeanList'][276]['availableDocks']
tot = result['stationBeanList'][276]['totalDocks']
bik = result['stationBeanList'][276]['availableBikes']
lat = result['stationBeanList'][276]['latitude']
lon = result['stationBeanList'][276]['longitude']
x2=41.793414
y2=-87.600

import math
from math import sqrt

dist = sqrt( (x2 - lat)**2 + (y2 - lon)**2 )


print ("The nearest Station to The Young Building is", nam, "and has a station ID of",ide)
print ("The longitude is", lon)
print ("There are",tot, "Docks and",ava, "available")
print ("There are",bik, "available bikes")
print ("The latitude is:", lat)
print ("The longitude is:", lon)
print ("The distance between the young bulding the nearest divvy bike station is;", dist)


