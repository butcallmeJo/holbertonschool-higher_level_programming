

class TaskModel():
	"""docstring for TaskModel"""
	def __init__(self, title):
		#TODO comments + stuff
		if title == None or not isinstance(title, str):
			raise Exception("string is not a string")

		self.__title = title

	def __str__(self):
		#TODO stuff
		return self.__title 

	def set_callback_title(self, func):
		#TODO stuff
		self.callback_title = func

	def get_title(self):
		#read name of func...
		return self.__title

	def toggle(self):
		return title[::-1]
		#TODO add exemption for below \/
		self.callback_title(self.__title)
