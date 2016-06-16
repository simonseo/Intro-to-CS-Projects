from Cards import Card
from Cards import Deck

class Hand(Deck):
	def __init__(self, name):
		Deck.__init__(self)
		self.__deckList = []
		self.__name = name
		self.value = [11,2,3,4,5,6,7,8,9,10,10,10,10]

	def add(self,card):
		self.__deckList.append(card)

	def sum(self):
		total = 0
		aceCount = 0
		for card in self.__deckList:
			total += value[card.rankList.index(card.rank)]
			if card.rank == 'Ace':
				aceCount += 1

		while aceCount > 0 and total > 21:
			total += 10
		return total

	def printDeck(self): 
		for card in self.__deckList:
			print(card)



class Blackjack:
	def __init__(self):
		self.__house = Hand('house')
		self.__player = Hand('player')
		self.__cards = Deck()

		self.__cards.deal(self.__house, 2)
		self.__house.__deckList[0].status = 'not hidden'
		self.__cards.deal(self.__player, 2)
		for card in self.__player.__deckList:
			card.status = 'not hidden'

	def ask(self):
		answer = input('HIT OR STAND? ')
		while not (answer.lower() == 'hit' or answer.lower() == 'stand'):
			answer = input('ERROR. HIT OR STAND? ')
		return answer

	def printBoard(self):
		print('House')
		print()

	def main(self):


		answer = self.ask()
		while answer.lower() == 'hit':
			self.__cards.deal(self.__player, 1)
			if self.__player.sum() >= 21:
				break
			answer = self.ask()

		while self.__house.sum() < 17:
			self.__cards.deal(self.__house, 1)








