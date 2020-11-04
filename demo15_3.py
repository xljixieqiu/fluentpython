class LookingGlass:
	def __enter__(self):
		import sys
		self.original_wirte=sys.stdout.write
		sys.stdout.write=self.reverse_write
		return 'JABBERWOCKY'

	def reverse_write(self,text):
		self.original_wirte(text[::-1])

	def __exit__(self,exc_type,exc_value,traceback):
		import sys
		sys.stdout.write=self.original_wirte
		if exc_type is ZeroDivisionError:
			print('Please Do Not divide by zero')
			return True
with LookingGlass() as what:
	print('good morning')
	print(what)
print(what)