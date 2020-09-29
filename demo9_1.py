from array import array
import math
class Vector2d:
	typecode='d'
	def __init__(self,x,y):
		self.__x=float(x)
		self.__y=float(y)
	def __repr__(self):
		name=type(self).__name__
		return '{}({!r},{!r})'.format(name,self.x,self.y)
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __eq__(self,other):
		return tuple(self)==tuple(other)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
	def __abs__(self):
		return math.hypot(self.x,self.y)
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode=chr(octets[0])
		memv=memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def angele(self):
		return math.atan2(self.y,self.x)
	def __format__(self,fmt_spec=''):
		if fmt_spec.endswith('p'):
			fmt_spec=fmt_spec[:-1]
			coords=(abs(self),self.angele())
			out_fmt='<{},{}>'
		else:
			coords=self
			out_fmt='({},{})'
		contents=(format(c,fmt_spec) for c in coords)
		return out_fmt.format(*contents)
	@property#将方法标记成属性
	def x(self):
		return self.__x
	@property
	def y(self):
		return self.__y
	def __hash__(self):
		return hash(self.x)^hash(self.y)
v1=Vector2d(3,4)
print(v1)
print(v1.x,v1.y)
print(repr(v1))
print(bytes(v1))
print(bool(v1))
print(abs(v1))
'''
print(ord('d'))
print(bytes([ord('d')]))
print(array('d',(3,4)))
print(bytes(array('d',(3,4))))
'''
print(Vector2d.frombytes(b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'))
print(format(v1,'.5fp'))
print(format(v1,'.5f'))
print(hash(v1))
print(v1.__dict__)