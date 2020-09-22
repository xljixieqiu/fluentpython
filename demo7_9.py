def make_avg():
	series=[]
	def averager(new_value):
		series.append(new_value)
		total=sum(series)
		return total/len(series)
	return averager
avg=make_avg()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)#审查averager对象中保存的局部变量
print(avg.__code__.co_freevars)#审查averager对象中保存的自由变量
print(avg.__closure__)#__closure__中的各个元素对应__code__.co_freevars中的各个名称
print(avg.__closure__[0].cell_contents)#__closure__中的元素是cell对象，有个cell_contents属性，保存着真正的值