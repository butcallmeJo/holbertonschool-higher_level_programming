import threading
class ReverseStrThread(threading.Thread):
	"""docstring for ReverseStrThread"""
	sentence = ""
	lock = threading.Lock()

	def __init__(self, word):
		threading.Thread.__init__(self)
		if not isinstance(word, str):
			raise Exception("word is not a string")
		self.word = word

	def run(self):
		reverse = self.word[::-1]
		ReverseStrThread.lock.acquire()
		ReverseStrThread.sentence += reverse + " "
		ReverseStrThread.lock.release()
