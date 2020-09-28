import weakref
s1={1,2,3}
s2=s1
def bye():
	print('Gone with the wind...')
ender=weakref.finalize(s1,bye)#finalize持有{1,2,3}的弱引用
print(ender.alive)
del s1
print(ender.alive)
s2=1#重新绑定s2，使{1,2,3}无法被获取到
print(ender.alive)