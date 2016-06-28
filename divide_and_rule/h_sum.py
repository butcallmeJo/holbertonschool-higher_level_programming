from threading import Thread, Lock, active_count
import sys

lock = Lock()

class Sum:
	"""docstring for Sum"""
    total = 0

    def __init__(self, nb_threads, numbers):
        Sum.total = 0
        if not isinstance(nb_threads, int):
            raise Exception("nb_threads is not an integer")
        if not isinstance(numbers, list) or not all(isinstance(i, int) for i in numbers):
            raise Exception("numbers is not an array of integers")
        piece = int(len(numbers) / nb_threads)
        for nb in range(nb_threads - 1):
            thread = SumThread(numbers[piece * nb:piece * (nb + 1)])
            thread.start()
        thread = SumThread(numbers[piece * (nb_threads - 1):])
        thread.start()

    def isComputing(self):
        if active_count() == 1:
            return False
        return True

    def __str__(self):
        with lock:
            return str(Sum.total)

class SumThread(Thread):
	"""docstring for SumThread"""

    def __init__(self, numbers):
        self.numbers = numbers
        Thread.__init__(self)

    def run(self):
        with lock:
            Sum.total += sum(self.numbers)
