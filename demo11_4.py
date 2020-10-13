import collections
from random import shuffle
Card=collections.namedtuple('Card',['rank','suit'])
class FrenchDeck:
	ranks=[str(n) for n in range(2,11)]+list('JQKA')
	suits='spades diamonds clubs hearts'.split()
	def __init__(self):
		self._cards=[Card(rank,suit) for rank in self.ranks
									 for suit in self.suits]
	def __len__(self):
		return len(self._cards)

	def __getitem__(self,index):
		return self._cards[index]
def set_card(deck,index,card):#猴子补丁
	deck._cards[index]=card
FrenchDeck.__setitem__=set_card#给FrenchDeck类的__setitem__属性赋值。
fdeck=FrenchDeck()

shuffle(fdeck)
print(fdeck[:])
print(len(fdeck))