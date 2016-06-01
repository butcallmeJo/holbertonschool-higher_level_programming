import json
from xml.dom.minidom import getDOMImplementation, Document

class Car():
	"""docstring for Car"""
	def __init__(self, *args, **kwargs):
		if len(args) > 0 or isinstance(args, dict):
			init_dict = args[0]
		else:
			init_dict = kwargs

		if not init_dict.get('name') or not isinstance(init_dict.get('name'), str):
			raise Exception("name is not a string")
		if not init_dict.get('brand') or not isinstance(init_dict.get('brand'), str):
			raise Exception("brand is not a string")
		if not init_dict.get('nb_doors') or not isinstance(init_dict.get('nb_doors'), int) or init_dict['nb_doors'] < 1:
			raise Exception("nb_doors is not > 0")

		self.__name = init_dict.get('name')
		self.__brand = init_dict.get('brand')
		self.__nb_doors = init_dict.get('nb_doors')

	def __str__(self):
		return self.__name + " " + self.__brand + " (" + str(self.__nb_doors) + ")"

	def get_name(self):
		return self.__name

	def get_brand(self):
		return self.__brand

	def get_nb_doors(self):
		return self.__nb_doors

	def set_nb_doors(self, number):
		self.__nb_doors = number

	def to_hash(self):
		hashed = {
			'name': self.__name,
			'brand': self.__brand,
			'nb_doors': self.__nb_doors
		}
		return hashed

	def to_json_string(self):
		return json.dumps(self.to_hash())

	def to_xml_node(self, doc):
		car = doc.createElement('car')
		car.setAttribute('nb_doors', self.__nb_doors)
		car.appendChild(doc)
		name = doc.createElement('name')
		name_content = doc.createTextNode(self.__name)
