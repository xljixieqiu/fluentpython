class HauntedBus:
	'''备受幽灵乘客折磨的校车'''
	def __init__(self,passengers=[]):
		self.passengers=passengers
	def pick(self,passenger):
		self.passengers.append(passenger)
	def drop(self,passenger):
		self.passengers.remove(passenger)
bus1=HauntedBus(['clack','bill'])
print(bus1.passengers)
bus2=HauntedBus()
bus2.pick('ann')
print(bus2.passengers)
bus3=HauntedBus()#此时初始列表不为空，里面有个ann。因为bus2.passengers和bus3.passengers指向同一个列表
print(bus3.passengers)