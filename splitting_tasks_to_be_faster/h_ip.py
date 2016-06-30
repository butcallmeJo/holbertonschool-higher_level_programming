import threading
import requests
import json

class IPThread(threading.Thread):
	"""docstring for IPThread"""
	def __init__(self, ip, callback):
		threading.Thread.__init__(self)
		self.ip = ip
		self.callback = callback

	def run(self):
		print "Search: " + self.ip
		url = "https://api.ip2country.info/ip?" + str(self.ip)
		resp = requests.get(url)
		print resp.json()['countryName']
		self.callback(resp.json()['countryName'])
