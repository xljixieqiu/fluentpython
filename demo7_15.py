import time
def clock(func):
	def clocked(*args):
		t0=time.perf_counter()
		result=func(*args)
		elapsed=time.perf_counter()-t0
		name=func.__name__
		arg_str=','.join(repr(arg) for arg in args)
		print('arg_str:%s,arg:%s'%(arg_str,args))
		print('[%.8fs] %s(%s)->%r'%(elapsed,name,arg_str,result))
		return result
	return clocked
@clock
def snooze(seconds):
	time.sleep(seconds)
@clock
def factorial(n):
	return 1 if n <2 else n*factorial(n-1)
@clock
def sum_data(n):
	return sum(i for i in range(n+1))
if __name__=='__main__':
	print('*'*40,'Calling snooze(.123)')
	snooze(.123)
	print('*'*40,'Calling factorial(6)')
	print('6!=',factorial(6))
	print('*'*40,'Calling sum_data(6)')
	print(sum_data(6))
	print(factorial.__name__)