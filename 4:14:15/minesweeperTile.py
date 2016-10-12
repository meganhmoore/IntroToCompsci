import random

class Tile:
	def __init__(self,row = 10,col = 10, value = ' ', state = 'H'):
		self.row= row
		self.col= col
		self.value = value
		self.state = state
	
	def __str__(self):
		if self.state == 'H':
			return '-'
		elif self.state == 'S':
			return self.value


class Minesweeper:
	#coveredTile=(width*height)-mines

	def __init__(self, mines = 15, width = 10, height = 10): #fill board with tiles
		self.board = []
		self.mines = mines
		self.width = width
		self.height = height
		self.assignMines(mines)
		self.assignNumbers()

	def assignMines(self, mines):
		for r in self.width:
			for c in self.height:
				self.board.append(Tile(r,c,0,'H'))
		random.shuffle(self.board)
		for i in range(mines):
			while(self.getTile(row,col).value == '*'):
				row = random.randint(0,self.height-1)
				col = random.randint(0,self.width-1)
			self.getTile(row,col).value='*'
		
	def uncover(self,row,column):
		self.getTile(row,column).state = 'S'

	def flagMine(self,row,column):
		if userFlag == 1:
			self.getTile(row,col).state = 'F'
		if userFlag==0:
			self.getTile(row,col).state='S'

	def __str__(self): #print board, called by print(minesweeper)
		for r in row:
			for c in col:
				if self.getTile(r,c).state == 'H':
					print('-', end=' ')
				elif self.getTile(r,c).state == 'F':
					print('F', end=' ')
				else:
					print(self.getTile(r,c).value, end= ' ')
		print()

	#def assignMines(self, mines):
		#tile = getTile(row,col)
		#for number in range(mines):
		#	tile = '*'

	def assignNumbers(self):
		n = 0
		for row in range(10):
			for col in range(10):
				tile=getTile(row,col)
				if tile.value != '*':
					if getTile(row-1,col-1).value == '*':
						n+=1
					if getTile(row-1,col).value == '*':
						n+=1
					if getTile(row-1,col+1).value =='*':
						n+=1
					if getTile(row,col-1).value == '*':
						n+=1
					if getTile(row,col+1).value == '*':
						n+=1
					if getTile(row+1,col-1).value == '*':
						n+=1
					if getTile(row+1,col).value =='*':
						n+=1
					if getTile(row+1,col+1).value == '*':
						n+=1
				tile.value = n
				if n == 0:
					tile.value = ' '
		

	def getTile(self,row,column):
		#self.row= row
		#self.col= col
		for tile in self.board:
			if tile.row == row and tile.col == col:
				return tile





print(Minesweeper)

userRow = int(input('Input row number: '))
userCol = int(input('Input column number: '))
userFlag = int(input('Would you like to uncover the square or flag it? (Uncover: 0 Flag: 1): '))
