from inspect import getgeneratorstate
class DemoException(Exception):
	""""为这次演示定义的异常类型"""

def demo_exc_handing():
	print('-> coroutine started')
	while True:
		try:
			x=yield
		except DemoException:
			print('*****DemoException handled.continuing****')
		else:
			print('-> coroutine received:{!r}'.format(x))
	raise RuntimeError('this line should never run')

exc_coro=demo_exc_handing()
next(exc_coro)
exc_coro.send(54)
exc_coro.throw(DemoException)
exc_coro.close()

print(getgeneratorstate(exc_coro))