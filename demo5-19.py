from inspect import signature
def clip(text:str,max_len:'int>0'=80) ->str:
	'''在max_len前面或后面的第一个空格处截断文本'''
	end=None
	if len(text)>max_len:
		space_before=text.rfind(' ',0,max_len)
		if space_before>=0:
			end=space_before
		else:
			space_after=text.rfind(' ',max_len)
			if space_after>=0:
				end=space_after
	if end is None:
		end=len(text)
	return text[:end].rstrip()
print(clip.__annotations__)
#output {'text': <class 'str'>, 'max_len': 'int>0', 'return': <class 'str'>}


#demo5-20
sig=signature(clip)
print('sig.return_annotation :',sig.return_annotation)
print(sig.parameters)
print(sig.parameters.values())
for param in sig.parameters.values():
	#print(param.annotation)
	#print(type(param.annotation))
	#print(type(repr(param.annotation)))
	print(repr(param.annotation).rjust(13),':',param.name,'=',param.default)