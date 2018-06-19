import unittest
from vec import Vec

class TestVecMethods(unittest.TestCase):

	def test_sub(self):
		vec = Vec(10,0) - Vec(5,0)	
		self.assertEqual(vec, Vec(5,0))
		
	def test_sub(self):
		vec = Vec(10,0) - Vec(5,0)	
		self.assertEqual(vec, Vec(5,0))
				
	def test_mul(self):
		vec = Vec(10,0) * Vec(5,0)	
		self.assertEqual(vec, Vec(50,0))
	def test_sub(self):
		vec = Vec(10,0) / Vec(5, 1)	
		self.assertEqual(vec, Vec(2,0))
		
	def test_sub(self):
		self.assertEqual(Vec(10,5).square(), Vec(100,25))	
		
	def test_distance(self):
		self.assertEqual(Vec(0,4).distance(Vec(0,0)), 4)
		self.assertEqual(Vec(3,0).distance(Vec(0,0)), 3)
		self.assertEqual(Vec(3,4).distance(Vec(0,0)), 5)
		
if __name__ == '__main__':
	unittest.main()