import weakref
a_set={0,1}
wref=weakref.ref(a_set)
print(wref)
print(wref())
a_set={2,3,4}
print(wref())#{0,1}对象不存在了 所以返回None
print(wref() is None)