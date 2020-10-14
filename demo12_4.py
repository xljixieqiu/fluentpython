class A:
	def ping(self):
		print('ping:',self)

class B(A):
	"""docstring for B"""
	def pong(self):
		print('pong:',self)

class C(A):
	def pong(self):
		print('PONG:',self)

class D(B,C):
	def ping(self):
		super().ping()
		print('post-ping:',self)
	def pingpong(self):
		self.ping()
		super().ping()
		self.pong()
		super().pong()
		C.pong(self)#需要显式传入self参数
d=D()
d.pong()
C.pong(d)
print(D.__mro__)
d.ping()
d.pingpong()
		