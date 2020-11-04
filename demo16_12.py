from inspect import getgeneratorstate
class DemoException(Exception):
	'''演示用'''

def demo_finally():
	print('-> coroutine started')
	try:
		while True:
			try:
				x=yield
			except DemoException:
				print('***DemoException handled,coroutine***')
			else:
				print('-> coroutine received {!r}'.format(x))
	finally:
		print('-> coroutine ending')

exc_coro=demo_finally()
next(exc_coro)
exc_coro.send('nihao')
exc_coro.throw(ZeroDivisionError)