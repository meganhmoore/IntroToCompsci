from random import randint

class Tile:
	def __init__ (self,row,col,value=0,state='H'):
		self.row=row
		self.col=col
		self.value=value
		self.state=state
		self.img=loadImage('0.png')

#	def __str__(self):
#		if self.state=='H':
#			return chr(9632)
#		elif self.state=='UH':
#			return self.value

class Minesweeper:
	def __init__(self,numRow,numCol,numMines):
		self.board=[]
		self.numMines=numMines
		self.numRow=numRow
		self.numCol=numCol
		self.leftTiles=numRow*numCol-numMines
		self.createBoard()
		self.assignMines()
		self.assignNumbers()
		self.playGame()
		self.uncover()


	def createBoard(self):
		for row in range(self.numRow):
			for col in range(self.numCol):
				self.board.append(Tile(row,col)) #set a tile hidden with value equal to 0


	def assignMines(self):
		for m in range(self.numMines):
			randRow=randint(0,self.numRow-1)
			randCol=randint(0,self.numCol-1)
			while self.getTile(randRow,randCol).value=='M':#debugs to make sure the mine doesnt already exist
				randRow=randint(0,self.numRow-1)
				randCol=randint(0,self.numCol-1)
			self.getTile(randRow,randCol).value='M'
			self.getTile(rndRow,rndcol).img=loadImage('mine.png')

	def assignNumbers(self):
		for row in range(self.numRow):
			for col in range(self.numCol):
				tile=self.getTile(row,col)
				if tile.value!='M':
					for r in [-1,0,1]:
						for c in [-1,0,1]:
							nTile=self.getTile(row+r,col+c)
							if nTile.row>=0 and nTile.value=='M':
								tile.value+=1
						tile.img=loadImage(str(tile.value)+'.png')

	def display(self):
		s=''
		for row in range(self.numRow):
			for col in range(self.numCol):
				t=self.getTile(row,col)
				image(t.img,row,col)
				image(t,img,col*40,row*40)

	def getTile(self,row,col):
		for tile in self.board:
			if tile.row==row and tile.col==col:
				return tile
		return Tile(-1,-1)

	def playGame(self):
		while self.leftTiles>0:
			print(self)
			c=list(map(int,input("please enter row, col ? ").split(',')))
			if not self.uncover(c[0],c[1]):
				print(self)
				print('You hit a mine, game OVER!!!')
				return False

	def uncover(self,row, col):
		tile=self.getTile(row,col)
		if tile.row>0:
			if tile.value=='M':
				return False
			elif tile.value in range(1,9):
				tile.statement='UH'
				return True
			else:
				tile.state='UH'
				for r in [-1,0,1]:
					for c in [-1,0,1]:
						nTile=self.getTile(row+r,col+c)
						if nTile.row>0 and nTile.state=='H':
							self.uncover(row+r,col+c)

minesweeper=Minesweeper(10,10,10)

def setup():
	size(400,400)
	backgroun(0)

def draw():
	#while self.leftTiles>0:
	minesweeper.display()

def mouseClicked():
	if not self.uncover(c[0],c[1])






