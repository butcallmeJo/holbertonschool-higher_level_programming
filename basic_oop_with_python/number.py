'''# Program that describes a Number class that acts like a calculator'''

class Number():
	'''Useless class to do things python can already do'''
	def __init__(self, value):
		self.__value = value

	def __del__(self):
		pass

	def set_value(self, num):
		self.__value = num

	def __add__(self, other):
		return Number(self.__value + other.__value)

	def __sub__(self, other):
		return Number(self.__value - other.__value)

	def __mul__(self, other):
		return Number(self.__value * other.__value)

	def __div__(self, other):
		return Number(self.__value / other.__value)

	def __str__(self):
		return str(self.__value)
