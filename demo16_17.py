from collections import namedtuple
Result=namedtuple('Result','count average')

#子生成器
def average():
	total=0
	count=0
	average=None
	while True:
		term =yield
		if term is None:
			break
		total+=term
		count+=1
		average=total/count
	return Result(count,average)

#委派生成器
def grouper(result,key):
	while True:
		result[key]=yield from average()

#客户端代码，调用方
def main(data):
	results={}
	for key,values in data.items():
		group=grouper(results,key)
		next(group)
		for value in values:
			group.send(value)
		group.send(None)
	print(results)
	report(results)

#输出报表
def report(results):
	for key,result in results.items():
		group,unit=key.split(';')
		print('{:2} {:5} averaging {:.2f}{}'.format(result.count,group,result.average,unit))

data={
'girls;kg':[40.6,22.6,75.5,34.6,55.5,77.5,33.3,44.4],
'girls;m':[1.4,1.6,1.66,1.77,1.45,1.66,1.57]
}

if __name__=='__main__':
	main(data)