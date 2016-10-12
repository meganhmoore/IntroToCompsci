import random
from copy import copy

class Game:

    def __init__(self, w, h):
        self.w = w
        self.h = h


class Tile:

    def __init__(self, row, col, value,rImg):
        self.value = value
        self.row = row
        self.col = col
        self.x=x
        self.y=y
        self.rImg=loadImage(rImg)


    def __str__(self):
        return str(self.value)
    
    def display(self):
        if self.value<16:
            image('Slide.png',self.col*100,self.row*100,100,100,self.x,self.y,self.x+100,self.y+100)
        
            
            
            


class Puzzle:

    neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, row, col):
        self.board = []
        self.row = row
        self.col = col
        #self.gRow=int(input('Please choose the row of the tile you would like to swap: '))
        #self.gCol=int(input('Please chose the column of the tile you would like to swap: '))
        self.createBoard()
        self.shuffleTile()
       # self.rImg = loadImage(rImg)
    #  self.move()

    def createBoard(self):
        n = 0
        for r in range(self.row):
            for c in range(self.col):
                n += 1
                self.board.append(Tile(r, c, 0, 'Slide.png'))
                self.getTile(r, c).value = n
        self.getTile(self.row - 1, self.col - 1).value = 'O'
        

    def __str__(self):
        s = ''
        for r in range(self.row):
            for c in range(self.col):
                if (r + 1 * c + 1) < 10:
                    s += str(self.getTile(r, c)) + ' |'
                else:
                    s += str(self.getTile(r, c)) + '|'
            s += '\n'
        return s

    def shuffleTile(self):
        blank = ''
        for i in range(3):
            swaplist = []
            for tile in self.board:
                if tile.value == 'O':
                    blank = tile
            for r, c in Puzzle.neighbors:
                neighbor=self.getTile(blank.row+r,blank.col+c)
                if neighbor:
                    swaplist.append(neighbor)
                swap=random.choice(swaplist)
                v=swap.value
                w=blank.value
                blank.value=v
                swap.value=w
            print(self)

    def move(self):
        neighbors = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # blank=''
        # swaplist=[]
        # for tile in self.board:
        #     if tile.value == 'O':
        #       blank=tile
        # for r,c in Puzzle.neighbors:
        #     neighbor=self.getTile(blank.row+r,blank.col+c)
        #     if neighbor:
        #       swaplist.append(neighbor)

        gRow = int(
            input('Please choose a row to switch with the empty spot: '))
        gCol = int(
            input('Please choose a column to switch with the empty spot: '))

        while not self.getTile(gRow, gCol):
            gRow = int(
                input('Please choose a row to switch with the empty spot: '))
            gCol = int(
                input('Please choose a column to switch with the empty spot: '))
        for n in neighbors:
            blank = self.getTile(gRow + n[0], gCol + n[1])
            if blank and blank.value == 'O':

                tile = self.getTile(gRow, gCol)
                blank.value = copy(tile.value)
                tile.value = 'O'
            # self.board.append(self.getTile(gRow,gCol))
            # self.board.append(self.getTile(gRow+n[0],gCol+n[1])
        #  return self.board
            print(self)


#        getTile(r,c).row=getTile(r+n[0],c+n[1]).row:
#          getTile(r,c).row=getTile(r+n[0],c+n[1]).col
#          getTile(r+n[0],c+n[1]).col=c
#          getTile(r+n[0],c+n[1]).row=r

    def getTile(self, row, column):
        for tile in self.board:
            if tile.row == row and tile.col == column:
                return tile

    def gamePlay(self):
        print(self)
        while not self.winGame():
            self.move()
        print("You have won the game!")

    def winGame(self):
        n = 1
        for r in range(self.row):
            for c in range(self.col):
                if self.getTile(r, c).value == 'O':
                    pass
                elif self.getTile(r, c).value != n:
                    return False
                n += 1
        return True
    
    def display(self):
        for t in self.board:
            t.display()

puzzle = Puzzle(4, 4)
#puzzle.gamePlay()

# tile1=Tile(3,3,3)
# print(tile1)
# print(puzzle.getTile(3,3))
# puzzle.shuffleTile()
# print(puzzle)


def setup():
    size(400, 400)
    stroke(255)
    background(0)

def draw():
    background(0)
   # image(rImg,0,0,400,400,100,100)

