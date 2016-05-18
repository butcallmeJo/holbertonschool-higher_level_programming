'''# Program that describes a square with attributes.'''
class Square():
	'''
	Square defines a square by its side length, color, center
	and calculates its area as well as prints a square made of '*'
	'''
	def __init__(self, side_length):
		self.__side_length = side_length
		self.__color = "white"
		self.__center = [0, 0]
		self.name = "square"

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
		#calculates the area of square
		return self.__side_length ** 2

	def print_s(self):
		for i in range(self.__side_length):
			for j in range(self.__side_length):
				if (i == 0 or i == self.__side_length-1) and j != self.__side_length-1:
					print '*',
				elif j == self.__side_length-1:
					print '*'
				elif j == 0:
					print '*',
				else:
					print ' ',
