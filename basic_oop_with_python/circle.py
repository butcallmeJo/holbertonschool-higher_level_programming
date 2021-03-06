'''# Program that describes a circle with attributes.'''
import math

class Circle():
	'''
	Circle is a class that defines radius, center, color, name
	and calculates area of circle, finds intersection if 2 circles
	are called.
	'''
	def __init__(self, radius):
		self.__radius = radius
		self.__color = "white"
		self.__center = [0, 0]
		self.name = "circle"

	def __del__(self):
		pass

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color

	def get_center(self):
		return self.__center

	def set_center(self, center):
		self.__center = center

	def area(self):
		#calculates the area of circle
		return 3.14*self.__radius*self.__radius

	def intersection(self, c_bis):
		#finds if self intersects with c_bis
		distance = math.sqrt(abs(self.__center[0] - c_bis.__center[0]) + abs(self.__center[1] - c_bis.__center[1]))
		if distance < self.__radius:
			return True
		else:
			return False
