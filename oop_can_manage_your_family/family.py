'''TODO'''

class Person():
	"""TODO for Person"""

	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

		# TODO error checking
		if id < 0 or not isinstance( id, int ):
			raise Exception("id is not an integer")
		if first_name == None or not isinstance( first_name, str ):
			raise Exception("string is not a string")
		if not (isinstance( i , int ) for item in date_of_birth):
			raise Exception("date_of_birth is not a valid date")
		if not isinstance( genre, str ) or genre not in self.GENRES:
			raise Exception("genre is not valid")
		if not isinstance( eyes_color, str ) or eyes_color not in self.EYES_COLORS:
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
