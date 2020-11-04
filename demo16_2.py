from inspect import getgeneratorstate
def simple_coroutine2(a):
	print('-> started:a=',a)
	b=yield a#在赋值语句中，=右边的代码在赋值之前执行，即先执行yield a
	print('-> received:b=',b)
	c=yield a+b
	print('-> received:c=',c)
my_coro=simple_coroutine2(14)
print(getgeneratorstate(my_coro))
next(my_coro)
print(getgeneratorstate(my_coro))
my_coro.send(15)
my_coro.send(22)