import itertools
from demo11_9 import Tombola
from demo11_12 import BingoCage
class AddableBingoCage(BingoCage):
	def __add__(self,other):
		if isinstance(other,Tombola):
			return AddableBingoCage(self.inspect()+other.inspect())
		else:
			return NotImplemented

	def __iadd__(self,other):
		if isinstance(other,Tombola):
			other_iterable=other.inspect()
		else:
			try:
				other_iterable=iter(other)
			except TypeError:
				cls=type(self)
				msg="right operand in += must be {!r} or an iterable"
				raise TypeError(msg.format(cls.__name__))
		self.load(other_iterable)
		return self
vowels='AEIOU'
globe=AddableBingoCage(vowels)
print(globe.inspect())
globe_copy =globe
globe2=AddableBingoCage('XYZ')
globe+=globe2
print(len(globe.inspect()))
print(globe.inspect())
print(globe_copy is globe)
globe+=1