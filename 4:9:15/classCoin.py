from random import randint

class Coin: #defining the class
	def __init__ (self):
		self.__sideUp='Heads' #you have to initialize the coin with some attribute so that it can change
# similarly you could code this as:
#def__init__(self,initialSide):
#	self.sideUp=initialSide

#then to instantiate a coin, make it coin1.Coin('Heads')
	def tossCoin(self):
		if randint(0,1)==0:
			self.__sideUp='Heads'
		else:
			self.__sideUp='Tails'

		def getCoinSideUp(self):
			return self.__sideUp
	def __str__ (self):
		return "the coin side up is"+self.__sideUp

coin1=Coin()#a coin that follows the attributes of Coin and is seperate
coin2=Coin()

coin1.tossCoin()
coin2.tossCoin()

#print('Coin 1 toss is', coin1.getCoinSideUp(), 'and coing 2 toss is', coin2.getCoinSideUp())

