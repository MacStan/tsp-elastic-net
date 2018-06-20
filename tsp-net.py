import time
import json
import math
import matplotlib.pyplot as plt
from typing import List
from vec import Vec
		
map_json = open("map.json").read()
map = json.loads(map_json)

map = [Vec(x[0],x[1]) for x in map]
center = (50,50)

def getnet( net_size = 50, radius = 5):
	angle = 0.0
	net = []
	angle_turn = math.pi * 2 / net_size
	for each in range(net_size):
		net_point = Vec( center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle) )
		angle = angle + angle_turn
		net.append(net_point)
	return net

net = getnet()


def updatenet(net, k):
	a = 0.3
	b = 0.2
	new_net = []
	for each in range(0, len(net) ):
		new_value = Vec( net[each].x, net[each].y )
		new_value += getbeta(net[each], net[each-1], net[(each+1) % len(net)], b, k)
		new_value += getalfa(a, map, net[each], net, k)
		new_net.append(new_value)
		
	return new_net
	
def getalfa(a, map, node, net, k):
	new_value = Vec(0,0);
	for each in map:
		w = getweight(each, node, net, k)
		diff = each - node
		new_value += Vec(diff.x * w, diff.y * w)
	return new_value * a
	
	
def getbeta(node, prev_node, post_node, b, k):
	part = prev_node + post_node - Vec( node.x*2, node.y*2) 
	mul = b * k 
	return Vec(part.x *mul, part.y*mul)
	
	

	
def getweight( city : Vec, node : Vec, net : List[Vec], k):
	#print(city)
	numerator = fi( math.fabs( city.distance( node ) ), k)
	denominator = 0
	for each in net:
		denominator += fi( math.fabs( city.distance( each )), k)
	return numerator / denominator
	
def fi(d, k):
	return math.exp( (-1 * d * d) / (2 * k * k) )
	
	
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
net_graph, = ax.plot([x.x for x in net], [x.y for x in net], 'r+',)
ax.plot([x.x for x in map], [x.y for x in map], 'bo')
 
k = 2
for each in range(1000000):
	if( each % 25 == 0 ):
		k = k * 0.99
	#time.sleep(1)
	net = updatenet(net,k)
	net_graph.set_ydata([x.y for x in net])
	net_graph.set_xdata([x.x for x in net])
	fig.canvas.draw()


def getweights(net : List[Vec], map: List[Vec], k):
	weights = [[]] # type: List[List[Vec]]
	for each in net:
		for city in map:
			weights[-1].append( getweight( city, each , net, k))
		weights.append( [] )
	return weights
	