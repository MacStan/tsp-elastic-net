import math

class Vec:
	def enforcevec(self, vec):
		if not isinstance(vec, Vec):
			raise TypeError( "passed wrong type to Vec" )
			
	def __init__(self, a, b):
		self.x = a
		self.y = b
	
	def __add__(self, other : "Vec"):
		self.enforcevec(other)
		return Vec( self.x + other.x, self.y + other.y)
	
	def __sub__(self, other : "Vec"):
		self.enforcevec(other)	
		return Vec( self.x - other.x, self.y - other.y)
		
	def __mul__(self, other : "Vec"):
		if isinstance(other, Vec):
			return Vec( self.x * other.x, self.y * other.y)
		else:
			return Vec( self.x * other, self.y * other )
		
	def __truediv__(self, other : "Vec"):
		self.enforcevec(other)	
		return Vec( self.x / other.x, self.y / other.y)		
	
	def square(self):
		return Vec( self.x * self.x, self.y * self.y)		
	
	def __repr__(self):
		return f"x: {self.x}, y: {self.y} "
	
	def __eq__(self, other):
		if not isinstance(other, Vec):
			return False
		return self.x == other.x and self.y == other.y
		
	def distance(self , other :"Vec"):
		return math.sqrt( math.pow(self.x - other.x, 2) + math.pow(self.y - other.y,2))