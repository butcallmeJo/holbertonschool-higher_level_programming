import threading

class StrLengthThread(threading.Thread):
	"""docstring for StrLengthThread"""
	total_str_length = 0
	def __init__(self, word):
		if not isinstance(word, str):
			raise Exception("word is not a string")
		self.word = word
		threading.Thread.__init__(self)

	def run(self):
		StrLengthThread.total_str_length += len(self.word)
