# Program that describes a circle with attributes.

class Circle():

	def __init__(self, radius):
		self.__radius = radius

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
