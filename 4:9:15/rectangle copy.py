import point.Point(x,y)

class Rectangle:
	def __init__ (self, x=0,y=0,width=10,height=10):
		self.point=Point(x,y)
		self.width=width
		self.height=height

	def __str__ (self):
		return '({0},{1}),{2},{3}'.format(self.point.x, self.point.y,self.width,self.height)

	def rectangleGrow (self,grow):
		grow=int(input('How much would you like to grow your rectangle by? '))
		gWidth=width*grow
		gHeight=height*grow
		return Rectangle(x,y,gWidth,gHeight)

	def rectangleMove (self,xMove,yMove):
		xMove=int(input('how far would you like to move the rectangle on the x axis?'))
		yMove=int(input('how far would you like to move the rectangle on the y axis?'))
		newX=x+xMove
		newY=y+yMove

r1=Rectangle(10,5,100,50)
print(r1)
r1.grow(25,-10)
r1.move(-10,10)