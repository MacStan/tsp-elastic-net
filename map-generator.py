from random import random
import json

map = []

for each in range(10):
	map.append((random()*100, random()*100))

with open('map.json', 'w') as outfile:
	json.dump(map, outfile)