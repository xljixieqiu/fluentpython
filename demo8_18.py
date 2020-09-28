import weakref
class Cheese:
	def __init__(self,kind):
		self.kind=kind
	def __repr__(self):
		return 'Cheese(%s)'%self.kind
catalog=[Cheese('red leicester'),Cheese('tilsit'),Cheese('brie'),Cheese('parmesan')]
socket=weakref.WeakValueDictionary()
for cheese in catalog:
	socket[cheese.kind]=cheese#cheese引用了'parmesan'
print(list(socket.keys()))	
print(sorted(socket.keys()))
del catalog
print(sorted(socket.keys()))
del cheese
print(sorted(socket.keys()))