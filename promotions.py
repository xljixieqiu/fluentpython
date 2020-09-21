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