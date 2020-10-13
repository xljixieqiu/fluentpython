from random import randrange
from demo11_9 import Tombola
@Tombola.register#注册TombolaList为Tombola的虚拟子类
class TombolaList(list):
	def pick(self):
		if self:
			position=randrange(len(self))
			return self.pop(position)#这里为什么非要传个position进去  想不通  直接pop不就好了，抛出最后一个值
		else:
			raise LookupError('pick from an empty TombolaList')

	load=list.extend#TombolaList.load与list.extend一样

	def loaded(self):#因为list没有__bool__方法，所以不能像load那样，loaded=list.__bool__
		return bool(self)

	def inspect(self):
		return tuple(sorted(self))

print(issubclass(TombolaList,Tombola))
t=TombolaList(range(10))
print(isinstance(t,Tombola))
print(TombolaList.__mro__)#__mro__储存类的继承关系（方法解析顺序）。这个属性的作用是：按顺序列出类和其超类.
#从输出可以看出TombolaList.__mro__中没有Tombola，因此，TombolaList没有从Tombola继承任何方法
print(dir(list))