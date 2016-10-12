# Next step: make code read board file, process and assign to tile by char
class Tile:
  def __init__ (self,row,col,state="X"):
    self.row=row
    self.col=col
    self.state=state
class Game:
  def __init__ (self,w,h):
    self.w=w
    self.h=h
    self.board=[]
    #wall Image
    #self.enemies[]
    #self.fruits[]
    self.numRow=21
    self.numCol=38
  def createBoard(self):
    theBoard = open("board.csv","r")
    console.log(theBoard)
    for row in range(self.numRow):
      for col in range(self.numCol):
        self.board.append(Tile(row,col))
  def getTile(self,row, col):
    for tile in self.board:
      if tile.row==row and tile.col == col:
        return tile
    return Tile(-1,-1)
  def display(self):
    for row in range(self.numRow):
        for col in range(self.numCol):
            t = self.getTile(row,col)
            if t.state=='X': #wall borders are black
                stroke(0)
                rect(col*20,row*20,col*20+20,row*20+20)
            else: #path borders are white
                stroke(255)
                rect(col*20,row*20,col*20+20,row*20+20)
#add background image here

#    for e in self.enemies:
#      e.display()

#    for f in self.fruits:
#      f.display()


class Creature:
  def __init__(self,x,y,r,w,h,pImg,pDImg,rF):
    self.x=x
    self.y=y
    self.r=r
    self.w=w
    self.h=h
    self.vx=0#velocity
    self.vy=0#velocity
    self.dir=1
    self.pImg=loadImage(pImg)
    self.pLImg=image(loadImage(pImg),self.x,self.y,self.w,self.h,self.x+self.w,self.y,self.x,self.y+self.h)
    self.pDImg=loadImage(pDImg)
    self.pUImg=image(loadImage(pDImg),self.x,self.y,self.w,self.h,self.x,self.y+h,self.w,self.y)
    self.f=0
    self.rF=rF


  def display(self):
    self.update()
    ellipse(self.x,self.y,self,2*self.r,2*self.r)
    stroke(0)
    

class Pacman(Creature):
  def __init__(self,x,y,r,w,h,pImg,pUImg,rF):
      Creature.__init__(self,x,y,r,w,h,pImg,pUImg,rF)
      self.Keys={UP:False, LEFT:False, RIGHT:False, DOWN:False}

  def update(self):
    print("")
    
  def distance(self,other): #measures the distance from ghosts
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)


class Ghost(Creature):
  def __init__(self):
    print("")
    
  def update(self):
    print("")

class Food:
  def __init__(self,fImg,score,required):
    #self.fImg=
    #self.score=
    self.required=True

  def display(self):
    print("")

game=Game(760,420) #Each square is 20x20 -- creatures 40x40
pacman=Pacman(0,0,10,20,20,'pacman.png','pacmanDown.png',2)



def setup():
    size(game.w,game.h)
    background(0)
    stroke(255)
    frameRate(100)
    
def draw():
    background(0)
    game.display()
    #pacman.display()
    
def keyPressed():
    pacman.Keys[keyCode]=True
    
def keyReleased():
    pacman.Keys[keyCode]=False