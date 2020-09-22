def make_avg():
	count=0
	total=0
	def averager(new_value):
		nonlocal count,total
		count+=1
		total+=new_value
		return total/count
	return averager
avg=make_avg()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(10))
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
print(avg.__closure__[1].cell_contents)