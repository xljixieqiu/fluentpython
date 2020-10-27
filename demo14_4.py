import re
import reprlib
RE_WORD=re.compile('\w+')
class Sentence:
	def __init__(self,text):
		self.text=text
		self.words=RE_WORD.findall(text)

	def __repr__(self):
		return 'Sentence(%s)'%reprlib.repr(self.text)

	def __iter__(self):
		return SentenceIter(self.words)

class SentenceIter:
	def __init__(self,words):
		self.words=words
		self.index=0

	def __next__(self):
		try:
			value=self.words[self.index]
		except IndexError:
			raise StopIteration()
		self.index+=1
		return value

	def __iter__(self):
		return self
s=Sentence('good moring sir,i have a dream!')
print(s)
for word in s:
	print(word)
'''
it=iter(s)
#print(list(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(list(it))
print(next(it))

print(next(it))
print(next(it))'''