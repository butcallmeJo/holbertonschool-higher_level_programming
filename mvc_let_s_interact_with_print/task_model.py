

class TaskModel():
	"""docstring for TaskModel"""
	def __init__(self, title):
		# Basic init stuff
		if title == None or not isinstance(title, str):
			raise Exception("string is not a string")
		self.__title = title
		self.__callback_title = []

	def __str__(self):
		# Basic print output
		return self.__title

	def set_callback_title(self, func):
		# Basic callback setter
		self.__callback_title = func

	def get_title(self):
		#read name of func...
		return self.__title

	def toggle(self):
		self.__title = self.__title[::-1]
		#TODO add exemption for below \/
		self.__callback_title(self.__title)
