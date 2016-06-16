from random import shuffle 
ranklist=['King','Queen','Jack','10','9','8','7','6','5','4','3','2','Ace'][::-1]
suitlist=['Spades','Hearts','Diamonds','Clubs']

class Card:
	def __init__(self,rank='Ace',suit='Spades'):
		self.suit=suit
		self.rank=rank
		'Spades'>'Hearts'>'Diamonds'>'Clubs'
		'Ace'>'King'>'Queen'>'Jack'>'10'>'9'>'8'>'7'>'6'>'5'>'4'>'3'>'2'


	def __str__(self):
		return "{0} of {1}".format(self.rank, self.suit)

	def __eq__(self, target):
		if self.rank == target.rank and self.suit == target.suit:
			return True
		else:
			return False
	def __le__(self, target):
		if self.rank < target.rank:
			return True
		elif self.rank == target.rank and self.suit <= target.suit:
			return True
		else:
			return False
	def __ge__(self, target):
		if self.rank > target.rank:
			return True
		elif self.rank == target.rank and self.suit >= target.suit:
			return True
		else:
			return False
	def __lt__(self, target):
		if self.rank < target.rank:
			return True
		elif self.rank == target.rank and self.suit < target.suit:
			return True
		else:
			return False
	def __gt__(self, target):
		if self.rank > target.rank:
			return True
		elif self.rank == target.rank and self.suit > target.suit:
			return True
		else:
			return False
	def __ne__(self, target):
		if self.rank != target.rank and self.suit != target.suit:
			return True
		else:
			return False

class Deck:
	def __init__(self):
		self.deckList=[]
		for rank in ranklist:
			for suit in suitlist:
				self.deckList.append(Card(rank,suit))
		self.shuffle()

	def __str__(self):
		tmp=''
		for card in self.deckList:
			tmp += str(card) + '\n'
		return tmp

	def shuffle(self):
		shuffle(self.deckList)

	def deal(self):
		return self.deckList.pop()

'''
c1=Card('2','Clubs')
c2=Card('King','Diamonds')
c3=Card('King','Diamonds')
print(Deck())
print (c1, c2, c3, sep=',')
print(c2==c3)
print(Deck().deckList)
print((c1,c2,c3))
'''