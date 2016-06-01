
class Car():
	"""docstring for Car"""
	def __init__(self, *args, **kwargs):
		if not kwargs['name'] or not isinstance(kwargs['name'], str):
			raise Exception("name is not a string")
		if not kwargs['brand'] or not isinstance(kwargs['brand'], str):
			raise Exception("brand is not a string")
		if not kwargs['nb_doors'] or not isinstance(kwargs['nb_doors'], int) or kwargs['nb_doors'] < 1:
			raise Exception("nb_doors is not > 0")

		self.__name = kwargs['name']
		self.__brand = kwargs['brand']
		self.__nb_doors = kwargs['nb_doors']

	def __str__(self):
		return self.__name + " " + self.__brand + " (" + str(self.__nb_doors) + ")"

	def get_name(self):
		return self.__name

	def get_brand(self):
		return self.__brand

	def get_nb_doors(self):
		return self.__nb_doors

	def to_hash(self):
		hashed = {
			'name': self.__name,
			'brand': self.__brand,
			'nb_doors': self.__nb_doors
		}
