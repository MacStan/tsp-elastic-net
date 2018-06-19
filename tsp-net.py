import json
import math
import matplotlib.pyplot as plt
from typing import List
from vec import Vec
		
map_json = open("map.json").read()
map = json.loads(map_json)

map = [Vec(x[0],x[1]) for x in map]
#print(max( [x[0] for x in map] ))
#print(max( [x[1] for x in map] ))

#print(min( [x[0] for x in map] ))
#print(min( [x[1] for x in map] ))

center = (50,50)

def getnet( net_size = 10, radius = 5):
	angle = 0.0
	net = []
	angle_turn = math.pi * 2 / net_size
	for each in range(net_size):
		net_point = Vec( center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle) )
		angle = angle + angle_turn
		net.append(net_point)
	return net

net = getnet()

def newnet(cities, net, k):
	weights = getweights(net, k)
	a = 0.3
	b = 0.7
	
	
	
def getchanges():
	pass
	
def getchange():
	a = 0.3
	b = 0.7
	
def getweights(net : List[Vec], map: List[Vec], k):
	weights = [[]] # type: List[List[Vec]]
	for each in net:
		for city in map:
			weights[-1].append( getweight( city, each , net, k))
		weights.append( [] )
	print( weights ) 
	return weights
	
	
def getweight( city : Vec, node : Vec, net : List[Vec], k):
	print(city)
	numerator = fi( math.fabs( city.distance( node ) ), k)
	denominator = 0
	for each in net:
		denominator += fi( math.fabs( city.distance( each )), k)
	return numerator / denominator
	
def fi(d, k):
	return math.exp( (-1 * d * d) / (2 * k * k) )
	
	
getweights(net,map,2 )
plt.plot([x[0] for x in net], [x[1] for x in net], 'ro')
plt.plot([x[0] for x in map], [x[1] for x in map], 'ro')
plt.axis([0, 100, 0, 100])
plt.show()