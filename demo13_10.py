import functools
import math
import itertools
from array import array
import reprlib
import numbers
import operator
import itertools
class Vector:
	typecode='d'

	def __init__(self,components):
		self._components=array(self.typecode,components)

	def __iter__(self):
		return iter(self._components)

	def __repr__(self):
		components=reprlib.repr(self._components)
		values=components[components.find('['):-1]
		return 'Vector({})'.format(values)

	def __str__(self):
		return str(tuple(self))

	def __bytes__(self):
		return (bytes([ord(typecode)])+
			bytes(self._components))
	
	def __eq__(self,other):
		return (len(self)==len(other) and 
			all(a==b for a,b in zip(self,other)))

	def __hash__(self):
		hashs=(hash(x) for x in self)
		return functools.reduce(operator.xor,hashs,0)#当hashs为空时，返回0；非空时，0当做第一个参数加入运算

	def __abs__(self):
		return math.sqrt(sum(x*x for x in self))

	def __bool__(self):
		return bool(abs(self))

	def __len__(self):
		return len(self._components)

	def __getitem__(self,index):
		cls=type(self)
		if isinstance(index,slice):
			return cls(self._components[index])
		elif isinstance(index,numbers.Integral):
			return self._components[index]
		else:
			msg='{.__name__} indices must be integrs'
			raise TypeError(msg.format(cls))

	shortcut_names='xyzt'

	def __getattr__(self,name):
		cls=type(self)
		if len(name)==1:
			position=cls.shortcut_names.find(name)
			if 0<=position<len(self._components):
				return self._components[position]
		msg='{.__name__!r} object has no attribute {!r}'
		raise AttributeError(msg.format(cls,name))

	def angle(self,n):
		r=math.sqrt(sum(x*x for x in self[n:]))
		a=math.atan2(r,self[n-1])
		if (n==len(self)-1) and (self[-1]<0):
			return math.pi*2-a
		else:
			return a

	def angeles(self):
		return (self.angle(n) for n in range(1,len(self)))

	def __format__(self,fmt_spec=''):
		if fmt_spec.endswith('h'):
			fmt_spec=fmt_spec[:-1]
			coords=itertools.chain([abs(self)],self.angeles())
			out_fmt='<{}>'
		else:
			coords=self
			out_fmt='({})'
		components=(format(x,fmt_spec) for x in coords)
		return out_fmt.format(','.join(components))

	@classmethod
	def frombytes(cls,octets):
		typecode=chr(octets[0])
		memv=memoryview(octets[1:]).cast(typecode)
		return cls(memv)

	def __add__(self,other):#加法
		try:
			pairs=itertools.zip_longest(self,other,fillvalue=0.0)
			return Vector(a+b for a,b in pairs)
		except TypeError:
			return NotImplemented

	def __radd__(self,other):
		return self+other

	def __mul__(self,scalar):#乘法
		if isinstance(scalar,numbers.Real):
			return Vector([x*scalar for x in self])
		else:
			return NotImplemented

	def __rmul__(self,scalar):
		return self*scalar

	def __eq__(self,other):
		if isinstance(other,Vector):
			return (len(self)==len(other) and 
					all(a==b for a,b in zip(self,other)))
		else:
			return NotImplemented


v1=Vector((1,2,3,4))
v2=Vector((5,6))
v1_copy=v1
print(id(v1))
print(id(v1_copy))
v1+=Vector([3,4,5,6])
print(v1)
print(id(v1))
print(id(v1_copy))
'''
v1=Vector([1,2,3])
print(format(v1,'h'))
print(v1.x)
'''