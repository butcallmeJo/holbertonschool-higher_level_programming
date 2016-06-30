import threading
import urllib2

class LoripsumThread(threading.Thread):
	"""docstring for LoripsumThread"""
	def __init__(self, filename):
		threading.Thread.__init__(self)
		self.filename = filename

	def run(self):
		data = urllib2.urlopen('http://loripsum.net/api/1/short')
		with open(self.filename, 'ab+') as f:
			for line in data:
				f.write(line)
