from threading import Lock
from time import sleep
from random import randint

class Store:
	"""docstring for Store"""
	def __init__(self, item_number, person_capacity):
		self.space_inside_lock = Lock()
		self.item_number_lock = Lock()
		self.item_number = item_number
		self.person_capacity = person_capacity
		self.space_inside = self.person_capacity


	def enter(self):
		while True:
			self.space_inside_lock.acquire()
			if self.space_inside > 0:
				self.space_inside -= 1
				self.space_inside_lock.release()
				break
			self.space_inside_lock.release()

	def buy(self):
		sleep(randint(5,10))
		self.space_inside_lock.acquire()
		self.space_inside += 1
		self.space_inside_lock.release()
		if self.item_number < 0:
			self.item_number_lock.acquire()
			self.item_number -= 1
			self.item_number_lock.release()
			return True
		else:
			return False
