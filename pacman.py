class Game:
	def __init__ (self,w,h):
		self.w=w
		self.h=h
		#wall Image
		#self.enemies[]
		#self.fruits[]

	def display(self):
		#add background image here

#		for e in self.enemies:
#			e.display()

#		for f in self.fruits:
#			f.display()


class Creature:
	def __init__(self,x,y,r,w,h,rImg,rF):
		self.x=x
		self.y=y
		self.r=r
		self.w=w
		self.h=h
		self.vx=0#velocity
		self.vy=0#velocity
		self.dir=1
		self.rImg=loadImg(rImg)
		self.f=0
		self.rF=rF


	def display(self):
		self.update()
		ellipse(self.x,self.y,self,2*self.r,2*self.r)
		stroke(0)
		

class Pacman(Creature):
	def __init__(self,):


	def update(self):

	def distance(self,other): #measures the distance from ghosts
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)


class Ghost(Creature):
	def __init__(self):

	def update(self):


class Food:
	def __init__(self,fImg,score,required):
		self.fImg=
		self.score=
		self.required=True

	def display(self):


game=Game()
pacman=Pacman()



def setup():
    size(game.w,game.h)
    background(0)
    stroke(255)
    frameRate(100)
    
def draw():
    background(0)
    game.display()
    pacman.display()
    
def keyPressed():
    pacman.Keys[keyCode]=True
    
def keyReleased():
    pacman.Keys[keyCode]=False

