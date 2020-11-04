#内置类型不会调用子类覆盖的特殊方法
class DoppeDict(dict):
	def __setitem__(self,key,value):
		super().__setitem__(key,value*2)
dd=DoppeDict(one=1)#如果括号中改成'one'=1。会报错SyntaxError: keyword can't be an expression：关键字不能是一个表达式
print(dd)
dd['two']=2
print(dd)
dd.update(three=3)#继承自dict的__init__和update方法不会调用DoppeDict.__setitem__方法
print(dd)
class AnswerDict(dict):
	def __getitem__(self,key):
		return 42
ad=AnswerDict(a='foo')
print(ad['a'])
d={}
d.update(ad)#dict.update方法忽略了AnswerDict.__getitem__方法
print(d)
print(d['a'])