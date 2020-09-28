class TwilightBus:
	'''让乘客销声匿迹的车'''
	def __init__(self,passengers=None):
		if passengers is None:
			self.passengers=[]
		else:
			self.passengers=passengers#问题出在这里，self.passengers和passengers指向同一个list。self.passengers是passengers的别名
	def pick(self,name):
		self.passengers.append(name)
	def drop(self,name):
		self.passengers.remove(name)
basketball_team=['sue','tina','maya','diana','pat']
bus=TwilightBus(basketball_team)
bus.drop('tina')
bus.drop('pat')
print(bus.passengers)
print(basketball_team)#bus中下车的学生在basketball_team中消失了
class TwilightBus1:
	'''让乘客销声匿迹的车'''
	def __init__(self,passengers=None):
		if passengers is None:
			self.passengers=[]
		else:
			self.passengers=list(passengers)#建立一个副本。就不会出现上面的情况了
	def pick(self,name):
		self.passengers.append(name)
	def drop(self,name):
		self.passengers.remove(name)
bus=TwilightBus1(basketball_team)
bus.pick('tina')
bus.pick('pat')
print(bus.passengers)
print(basketball_team)