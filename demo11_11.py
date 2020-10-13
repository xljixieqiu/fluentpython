from demo11_9 import Tombola
class Fake(Tombola):
	def pick(self):
		return 12
f=Fake()#因为没有定义load()抽象方法 所以报错