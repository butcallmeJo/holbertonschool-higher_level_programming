'''TODO'''
import json
import os

class Person():
	"""TODO for Person"""

	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		'''init func for class Person. init variables and handles errors'''
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
		self.kind = self.__class__.__name__
		self.is_married_to = 0
		self.children = []

	def __del__(self):
		'''iono'''
		pass

	def get_first_name(self):
		'''read name of func'''
		return self.__first_name

	def __str__(self):
		'''prints first and last name'''
		return self.__first_name + " " + self.last_name

	def is_male(self):
		'''read name of func'''
		if self.__genre == "Male":
			return True
		else:
			return False

	def age(self):
		'''returns age of person'''
		# today = 5/20/2016...[5,20,2016]
		age_var = 2016-self.__date_of_birth[2] - ((5, 20) < (self.__date_of_birth[0], self.__date_of_birth[1]))
		return age_var

	def get_kind(self):
		'''returns wether person is adult, senior, teen or baby'''
		if self.kind != None:
			return self.kind
		else:
			return self.__class__.__name__

	def get_id(self):
		'''read name of func'''
		return self.__id

	def get_eyes_color(self):
		'''read name of func'''
		return self.__eyes_color

	def json(self):
		'''returns a dictionary of key value pairs'''
		dicc = {
			'id': self.__id,
			'first_name': self.__first_name,
			'last_name': self.last_name,
			'kind': self.get_kind(),
			'genre': self.__genre,
			'date_of_birth': self.__date_of_birth,
			'eyes_color': self.__eyes_color,
			'is_married_to': self.is_married_to,
			'children': self.children
			}
		return dicc

	def load_from_json(self, json):
		'''read name of func'''
		if not isinstance(json, dict):
			raise Exception("json is not valid")
		self.__id = json['id']
		self.__first_name = str(json['first_name'])
		self.last_name = str(json['last_name'])
		self.kind = str(json['kind'])
		self.__genre = str(json['genre'])
		self.__date_of_birth = json['date_of_birth']
		self.__eyes_color = str(json['eyes_color'])
		self.is_married_to = json['is_married_to']
		self.children = json['children']



	def __gt__(self, other):
		'''overloads cmp operators to compare ages of people'''
		return self.age() > other.age()

	def __lt__(self, other):
		'''overloads cmp operators to compare ages of people'''
		return self.age() < other.age()

	def __ge__(self, other):
		'''overloads cmp operators to compare ages of people'''
		return self.age() >= other.age()

	def __le__(self, other):
		'''overloads cmp operators to compare ages of people'''
		return self.age() <= other.age()

	def __eq__(self, other):
		'''overloads cmp operators to compare ages of people'''
		return self.age() == other.age()

	def __ne__(self, other):
		'''overloads cmp operators to compare ages of people'''
		return self.age() != other.age()


'''
Sub-Classes
'''

class Baby(Person):
	"""docstring for Baby"""

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		'''init func for class Baby. init variables'''
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		'''read name of func'''
		pass

	def can_run(self):
		'''returns true if person can run'''
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		'''return true if person need_help'''
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		'''return true if person is young'''
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		'''return true if person can vote'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def can_be_married(self):
		'''return true if person can marry'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def is_married(self):
		'''return true if person is married'''
		if self.is_married_to != 0:
			return True

	def divorce(self, p):
		'''divorces 2 persons'''
		self.is_married_to = 0
		p.is_married_to = 0

	def just_married_with(self, p):
		'''marries two persons together, but handles errors as well'''
		if (self.is_married_to != 0)  or (p.is_married_to !=0):
			raise Exception("Already married")
		if((not self.can_be_married()) or  (not p.can_be_married())):
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()
		if not self.is_male() and p.is_male():
			'''sets last name of female if and only if she marries a male'''
			self.last_name = p.last_name

	def can_have_child(self):
		'''return true if person can have child'''
		return isinstance(self, Adult)

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
		'''return a new baby based on parents'''
		if p is None or not (p.get_kind() == "Adult" or p.get_kind() == "Senior"):
			raise Exception("p is not an Adult of Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if first_name == None or not isinstance(first_name, str):
			raise Exception("string is not a string")
		if not ((0 < date_of_birth[0] < 13) and (0 < date_of_birth[1] < 32) and isinstance(12, int)):
			raise Exception("date_of_birth is not a valid date")
		if not isinstance(genre, str) or genre not in self.GENRES:
			raise Exception("genre is not valid")
		if not self.can_have_child() or not p.can_have_child():
			raise Exception("Can't have baby")

		if eyes_color == '':
			if self.get_eyes_color() == "Brown" or p.get_eyes_color() == "Brown":
				eyes_color = "Brown"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Blue":
				eyes_color = "Blue"
			elif self.get_eyes_color() == "Green" and p.get_eyes_color() == "Green":
				eyes_color = "Green"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Green":
				eyes_color = "Blue"

		b = Baby(id, first_name, date_of_birth, genre, eyes_color)
		b.last_name = self.last_name
		if id not in self.children:
			self.children.append(id)
		if id not in p.children:
			p.children.append(id)
		return b

	def adopt_child(self, c):
		'''makes adult or senior adopt a child'''
		if self is None or not isinstance(self, Adult) or not isinstance(self, Senior):
			raise Exception("Can't adopt child")
		elif c.get_id() not in self.children:
			self.children.append(c.get_id())

class Teenager(Person):
	"""docstring for Teenager"""

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		'''init func for class Baby. init variables'''
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		'''read name of func'''
		pass

	def can_run(self):
		'''returns true if person can run'''
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		'''return true if person need_help'''
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		'''return true if person is young'''
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		'''return true if person can vote'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def can_be_married(self):
		'''return true if person can marry'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def is_married(self):
		'''return true if person is married'''
		if self.is_married_to != 0:
			return True

	def divorce(self, p):
		'''divorces 2 persons'''
		self.is_married_to = 0
		p.is_married_to = 0

	def just_married_with(self, p):
		'''marries two persons together, but handles errors as well'''
		if (self.is_married_to != 0)  or (p.is_married_to !=0):
			raise Exception("Already married")
		if((not self.can_be_married()) or  (not p.can_be_married())):
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()
		if not self.is_male() and p.is_male():
			'''sets last name of female if and only if she marries a male'''
			self.last_name = p.last_name

	def can_have_child(self):
		'''return true if person can have child'''
		return isinstance(self, Adult)

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
		'''return a new baby based on parents'''
		if p is None or not (p.get_kind() == "Adult" or p.get_kind() == "Senior"):
			raise Exception("p is not an Adult of Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if first_name == None or not isinstance(first_name, str):
			raise Exception("string is not a string")
		if not ((0 < date_of_birth[0] < 13) and (0 < date_of_birth[1] < 32) and isinstance(12, int)):
			raise Exception("date_of_birth is not a valid date")
		if not isinstance(genre, str) or genre not in self.GENRES:
			raise Exception("genre is not valid")
		if not self.can_have_child() or not p.can_have_child():
			raise Exception("Can't have baby")

		if eyes_color == '':
			if self.get_eyes_color() == "Brown" or p.get_eyes_color() == "Brown":
				eyes_color = "Brown"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Blue":
				eyes_color = "Blue"
			elif self.get_eyes_color() == "Green" and p.get_eyes_color() == "Green":
				eyes_color = "Green"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Green":
				eyes_color = "Blue"

		b = Baby(id, first_name, date_of_birth, genre, eyes_color)
		b.last_name = self.last_name
		if id not in self.children:
			self.children.append(id)
		if id not in p.children:
			p.children.append(id)
		return b

	def adopt_child(self, c):
		'''makes adult or senior adopt a child'''
		if self is None or not isinstance(self, Adult) or not isinstance(self, Senior):
			raise Exception("Can't adopt child")
		elif c.get_id() not in self.children:
			self.children.append(c.get_id())

class Adult(Person):
	"""docstring for Adult"""

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		'''init func for class Baby. init variables'''
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		'''read name of func'''
		pass

	def can_run(self):
		'''returns true if person can run'''
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		'''return true if person need_help'''
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		'''return true if person is young'''
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		'''return true if person can vote'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def can_be_married(self):
		'''return true if person can marry'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def is_married(self):
		'''return true if person is married'''
		if self.is_married_to != 0:
			return True

	def divorce(self, p):
		'''divorces 2 persons'''
		self.is_married_to = 0
		p.is_married_to = 0

	def just_married_with(self, p):
		'''marries two persons together, but handles errors as well'''
		if (self.is_married_to != 0)  or (p.is_married_to !=0):
			raise Exception("Already married")
		if((not self.can_be_married()) or  (not p.can_be_married())):
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()
		if not self.is_male() and p.is_male():
			'''sets last name of female if and only if she marries a male'''
			self.last_name = p.last_name

	def can_have_child(self):
		'''return true if person can have child'''
		return isinstance(self, Adult)

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
		'''return a new baby based on parents'''
		if p is None or not (p.get_kind() == "Adult" or p.get_kind() == "Senior"):
			raise Exception("p is not an Adult of Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if first_name == None or not isinstance(first_name, str):
			raise Exception("string is not a string")
		if not ((0 < date_of_birth[0] < 13) and (0 < date_of_birth[1] < 32) and isinstance(12, int)):
			raise Exception("date_of_birth is not a valid date")
		if not isinstance(genre, str) or genre not in self.GENRES:
			raise Exception("genre is not valid")
		if not self.can_have_child() or not p.can_have_child():
			raise Exception("Can't have baby")

		if eyes_color == '':
			if self.get_eyes_color() == "Brown" or p.get_eyes_color() == "Brown":
				eyes_color = "Brown"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Blue":
				eyes_color = "Blue"
			elif self.get_eyes_color() == "Green" and p.get_eyes_color() == "Green":
				eyes_color = "Green"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Green":
				eyes_color = "Blue"
			elif self.get_eyes_color() == "Green" and p.get_eyes_color() == "Blue":
				eyes_color = "Blue"
			else:
				eyes_color = "Black"

		b = Baby(id, first_name, date_of_birth, genre, eyes_color)
		b.last_name = self.last_name
		if id not in self.children:
			self.children.append(id)
		if id not in p.children:
			p.children.append(id)
		return b

	def adopt_child(self, c):
		'''makes adult or senior adopt a child'''
		if self is None or not isinstance(self, Adult) or not isinstance(self, Senior):
			raise Exception("Can't adopt child")
		elif c.get_id() not in self.children:
			self.children.append(c.get_id())

class Senior(Person):
	"""docstring for Senior"""

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
		'''init func for class Baby. init variables'''
		Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)

	def __del__(self):
		'''read name of func'''
		pass

	def can_run(self):
		'''returns true if person can run'''
		return isinstance(self, Teenager) or isinstance(self, Adult)

	def need_help(self):
		'''return true if person need_help'''
		return isinstance(self, Baby) or isinstance(self, Senior)

	def is_young(self):
		'''return true if person is young'''
		return isinstance(self, Teenager) or isinstance(self, Baby)

	def can_vote(self):
		'''return true if person can vote'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def can_be_married(self):
		'''return true if person can marry'''
		return isinstance(self, Senior) or isinstance(self, Adult)

	def is_married(self):
		'''return true if person is married'''
		if self.is_married_to != 0:
			return True

	def divorce(self, p):
		'''divorces 2 persons'''
		self.is_married_to = 0
		p.is_married_to = 0

	def just_married_with(self, p):
		'''marries two persons together, but handles errors as well'''
		if (self.is_married_to != 0)  or (p.is_married_to !=0):
			raise Exception("Already married")
		if((not self.can_be_married()) or  (not p.can_be_married())):
			raise Exception("Can't be married")
		self.is_married_to = p.get_id()
		p.is_married_to = self.get_id()
		if not self.is_male() and p.is_male():
			'''sets last name of female if and only if she marries a male'''
			self.last_name = p.last_name

	def can_have_child(self):
		'''return true if person can have child'''
		return isinstance(self, Adult)

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
		'''return a new baby based on parents'''
		if p is None or not (p.get_kind() == "Adult" or p.get_kind() == "Senior"):
			raise Exception("p is not an Adult of Senior")
		if id < 0 or not isinstance(id, int):
			raise Exception("id is not an integer")
		if first_name == None or not isinstance(first_name, str):
			raise Exception("string is not a string")
		if not ((0 < date_of_birth[0] < 13) and (0 < date_of_birth[1] < 32) and isinstance(12, int)):
			raise Exception("date_of_birth is not a valid date")
		if not isinstance(genre, str) or genre not in self.GENRES:
			raise Exception("genre is not valid")
		if not self.can_have_child() or not p.can_have_child():
			raise Exception("Can't have baby")

		if eyes_color == '':
			if self.get_eyes_color() == "Brown" or p.get_eyes_color() == "Brown":
				eyes_color = "Brown"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Blue":
				eyes_color = "Blue"
			elif self.get_eyes_color() == "Green" and p.get_eyes_color() == "Green":
				eyes_color = "Green"
			elif self.get_eyes_color() == "Blue" and p.get_eyes_color() == "Green":
				eyes_color = "Blue"

		b = Baby(id, first_name, date_of_birth, genre, eyes_color)
		b.last_name = self.last_name
		if id not in self.children:
			self.children.append(id)
		if id not in p.children:
			p.children.append(id)
		return b

	def adopt_child(self, c):
		'''makes adult or senior adopt a child'''
		if self is None or not isinstance(self, Adult) or not isinstance(self, Senior):
			raise Exception("Can't adopt child")
		elif c.get_id() not in self.children:
			self.children.append(c.get_id())

'''
File Methods
'''

def save_to_file(list, filename):
	'''save a list of dictionaries to a json file'''
	list_of_json_strs = []
	with open(filename, 'w') as w_file:
		for i in list:
			list_of_json_strs.append(i.json())
		json.dump(list_of_json_strs, w_file)

def load_from_file(filename):
	'''returns a list of dictionaries coming from a json file'''
	if not isinstance(filename, str) or not os.path.isfile(filename):
		raise Exception("filename is not valid or doesn't exist")
	else:
		with open(filename, 'r') as datafile:
			data = json.load(datafile)
			if data == None:
				raise Exception("json is not valid")
			Persons = []
			for d in data:
				if d['kind'] == "Adult":
					p = Adult(0, "Jo", [6,7,1992], "Male", "Brown")
				elif d['kind'] == "Senior":
					p = Senior(0, "Jo", [6,7,1992], "Male", "Brown")
				elif d['kind'] == "Teenager":
					p = Teenager(0, "Jo", [6,7,1992], "Male", "Brown")
				elif d['kind'] == "Baby":
					p = Baby(0, "Jo", [6,7,1992], "Male", "Brown")
				p.load_from_json(d)
				Persons.append(p)
			return Persons
