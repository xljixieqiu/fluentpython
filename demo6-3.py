from collections import namedtuple
Customer=namedtuple('Customer','name fidetity')
class LineItem:
	def __init__(self,product,quantity,price):
		self.product=product
		self.quantity=quantity
		self.price=price
	def total(self):
		return self.quantity*self.price
class Order:
	def __init__(self,customer,cart,promotion=None):
		self.customer=customer
		self.cart=list(cart)
		self.promotion=promotion
	def total(self):
		if not hasattr(self,'__total'):
			self.__total=sum(item.total() for item in self.cart)
		return self.__total
	def due(self):
		if self.promotion is None:
			discount=0
		else:
			discount=self.promotion(self)
		return self.total()-discount
	def __repr__(self):
		fmt='<Order total:{:.2f} due:{:.2f}>'
		return fmt.format(self.total(),self.due())
def FidetityPromo(order):
	return order.total()*.05 if order.customer.fidetity>=1000 else 0
def BulkPromo(order):
	discount=0
	for item in order.cart:
		if item.quantity>=20:
			discount+=item.total()*.1
	return discount
def LargeOrderPromo(order):
	distinct_product={item.product for item in order.cart}
	if len(distinct_product)>=10:
		return order.total()*.07
	return 0
joe=Customer('John Doe',0)
ann=Customer('Ann Smith',1100)
cart=[LineItem('banana',5,.5),LineItem('apple',10,1.5),LineItem('watermellon',5,5.0)]
banana_cart=[LineItem('banana',20,.5),LineItem('apple',5,1.5)]
o1=Order(ann,cart,FidetityPromo)
print(o1)
o2=Order(joe,banana_cart,BulkPromo)
print(o2)
largeorder=[LineItem(str(item),1,1.0) for item in range(10)]
o3=Order(ann,largeorder,LargeOrderPromo)
print(o3)