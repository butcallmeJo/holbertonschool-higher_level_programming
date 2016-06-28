from sys import argv
from threading import Thread

class StrLengthThread(Thread):
	"""docstring for StrLengthThread"""
	def __init__(self, word):
		if not isinstance(word, str):
			raise Exception("word is not a string")
		self.word = word
		Thread.__init__(self)

	def run(self):
		global total_str_length
		total_str_length += len(word)

if len(argv) <= 1:
	raise Exception("Not enough arguments")
else:
	text = argv[1]
	words = text.split(" ")
	str_length_threads = []

	total_str_length = len(words) - 1
	for word in words:
	    str_length_thread = StrLengthThread(word)
	    str_length_threads += [str_length_thread]
	    str_length_thread.start()

	for t in str_length_threads:
	    t.join()

	print "%d" % total_str_length
