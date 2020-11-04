from functools import wraps
from inspect import getgeneratorstate
def coroutine(func):
	"""装饰器：向前执行到第一个'yield'表达式，预激'func'"""
	@wraps(func)
	def primer(*args,**kwargs):
		gen=func(*args,**kwargs)
		next(gen)
		return gen
	return primer

@coroutine
def average():
	total=0
	count=0
	average=None
	while True:
		term=yield average
		total+=term
		count+=1
		average=total/count

my_coro3=average()
print(getgeneratorstate(my_coro3))
print(my_coro3.send(10))