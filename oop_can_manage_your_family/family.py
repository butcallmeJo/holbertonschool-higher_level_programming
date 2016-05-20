'''TODO'''
import json
import os

class Person():
	"""TODO for Person"""

	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

		# TODO error checking
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if first_name == None or not isinstance(first_name, str):
			raise Exception("string is not a string")
		if not ((0 < date_of_birth[0] < 13) and (0 < date_of_birth[1] < 32) and isinstance(12, int)):
			raise Exception("date_of_birth is not a valid date")
		if not isinstance(genre, str) or genre not in self.GENRES:
			raise Exception("genre is not valid")
		if not isinstance(eyes_color, str) or eyes_color not in self.EYES_COLORS:
			raise Exception("eyes_color is not valid")

		self.__id = id
		self.__eyes_color = eyes_color
		self.__genre = genre
		self.__date_of_birth = date_of_birth
		self.__first_name = first_name
		self.last_name = "last_name"

	def __del__(self):
		pass

	def get_first_name(self):
		return self.__first_name

	def __str__(self):
		return self.__first_name + " " + self.last_name

	def is_male(self):
		if self.__genre == "Male":
			return True
		else:
			return False

	def age(self):
		# today = 5/20/2016...[5,20,2016]
		age_var = 2016-self.__date_of_birth[2] - ((5, 20) < (self.__date_of_birth[0], self.__date_of_birth[1]))
		return age_var

	def json(self):
		json = {'id': self.__id,
		'eyes_color': self.__eyes_color,
		'genre': self.__genre,
		'date_of_birth': self.__date_of_birth,
		'first_name': self.__first_name,
		'last_name': self.last_name}
		return json

	def load_from_json(self, json):
		if not isinstance(json, dict):
			raise Exception("json is not valid")
		self.__id = str(json['id'])
		self.__eyes_color = str(json['eyes_color'])
		self.__genre = str(json['date_of_birth'])
		self.__first_name = str(json['first_name'])
		self.last_name = str(json['last_name'])

	def __gt__(self, other):
		return self.age() > other.age()

	def __lt__(self, other):
		return self.age() < other.age()

	def __ge__(self, other):
		return self.age() >= other.age()

	def __le__(self, other):
		return self.age() <= other.age()

	def __eq__(self, other):
		return self.age() == other.age()

	def __ne__(self, other):
		return self.age() != other.age()


class Baby(Person):
	"""docstring for Baby"""

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		pass

	def can_run(self):
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		return isinstance(self, Senior) or isinstance(self, Adult)

class Teenager(Person):
	"""docstring for Teenager"""

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		pass

	def can_run(self):
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		return isinstance(self, Senior) or isinstance(self, Adult)

class Adult(Person):
	"""docstring for Adult"""

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		pass

	def can_run(self):
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		return isinstance(self, Senior) or isinstance(self, Adult)

class Senior(Person):
	"""docstring for Senior"""

	def __init__(self):
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		pass

	def can_run(self):
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		return isinstance(self, Senior) or isinstance(self, Adult)

def save_to_file(list, filename):
	file = open(filename, 'w+')
	file.write(list)
	file.close()

def load_from_file(filename):
	if not isinstance(filename, str) or not os.path.isfile(filename):
		raise Exception("filename is not valid or doesn't exist")
	file = open(filename, 'r')
	return file.read()
