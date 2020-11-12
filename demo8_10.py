import copy 
a=[10,20]
b=[a,30]
a.append(b)
print(a)
c=copy.copy(a)
print(c)
d=copy.deepcopy(a)
print(d)