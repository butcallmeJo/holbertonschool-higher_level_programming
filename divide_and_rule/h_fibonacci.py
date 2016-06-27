import threading

class FibonacciThread(threading.Thread):
	"""docstring for FibonacciThread"""

	def __init__(self, number):
		if not isinstance(number, int):
			raise Exception("number is not an integer")
		self.number = number
		threading.Thread.__init__(self)

	def run(self):
		first = 0
		second = 1

		for i in range(self.number):
			(first, second) = (second, first + second)

		print "" + str(self.number) + " => " + str(first) + ""
