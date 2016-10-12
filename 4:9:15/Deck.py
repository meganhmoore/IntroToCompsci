import cards
import random

class Deck:
	deck=[]

	def __init__ (self,rank=3,suit='Hearts'):
		self.rank={1:'Ace',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'Jack',12:'Queen',13:'King'}
		self.suit=['Hearts', 'Spades','Clubs','Diamonds']


		for s in suit:
			for r in range (13):
				self.card=Card(s,rank[r])
			deck.append(card)

	def shuffleCards(self):
		random.shuffle(deck)

	def dealCard(self):
