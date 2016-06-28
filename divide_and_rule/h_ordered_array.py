import threading

lock = threading.Lock()

class OrderedArray():
	"""docstring for OrderedArray"""
	def __init__(self):
		pass

	list = []

	def add(self, number):
		if not isinstance(number, int):
			raise Exception("number is not an integer")
		thread = OrderedArrayThread(number)
		thread.start()

	def isSorting(self):
		if threading.active_count() == 1:
			return False
		else:
			return True

	def __str__(self):
		return str(OrderedArray.list)

class OrderedArrayThread(threading.Thread):
	"""docstring for OrderedArrayThread"""
	def __init__(self, number):
		if not isinstance(number, int):
			raise Exception("number is not an integer")
		self.number = number
		threading.Thread.__init__(self)

	def run(self):
		with lock:
			OrderedArray.list +=[self.number]
			OrderedArray.list.sort()
