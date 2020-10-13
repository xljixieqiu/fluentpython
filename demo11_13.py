import random
from demo11_9 import Tombola
class LotteryBlower(Tombola):
	def __init__(self,iterable):
		self._balls=list(iterable)

	def load(self,iterable):
		self._balls.extend(iterable)

	def pick(self):
		try:
			position=random.randrange(len(self._balls))
		except ValueError:
			raise LookupError('pick from an empty LotteryBlower')
		return self._balls.pop(position)

	def loaded(self):
		return bool(self._balls)

	def inspect(self):
		return tuple(sorted(self._balls))