from functools import singledispatch
from collections import abc
import numbers
import html
@singledispatch
def htmlize(obj):
	content=html.escape(repr(obj))
	return '<pre>{}</pre>'.format(content)
@htmlize.register(str)
def _(text):
	content=html.escape(text).replace('\n','<br>\\n')
	return '<p>{}</p>'.format(content)
@htmlize.register(numbers.Integral)
def _(n):
	return '<pre>{0} (0x{0:x})</pre>'.format(n)
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
	content='</li>\n<li>'.join(htmlize(s) for s in seq)
	return '<ul>\n<li>{}</li>\n</ul>'.format(content)
print(htmlize({1,2,3}))
print(htmlize(abs))
print(htmlize('hhhtm \n hsdh'))
print(htmlize(42))
print(htmlize(['alpha',66,{3,2,1}]))