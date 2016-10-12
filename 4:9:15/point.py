class Point:
	#point class represents and manipulates x,y coords.
	def __init__ (self,x=0,y=0):
		#creates a point with (x,y), default is at origin
		self.x=x
		self.y=y

	def distanceFromOrigin(self):
		#computes the distance between the point and the origin (0,0)
		return((self.x**2)+(self.y**2))**0.5

	def __str__ (self):
		return "({0},{1})".format(self.x,self.y)	


	def halfway(self, target):
		mx=(self.x+target.x)/2
		my=(self.y+target.y)/2
		return Point(mx,my)
def midpoint(p1,p2):
	#returns the midpoint between the two points
	mx=(p1.x+p2.x)/2
	my=(p1.y+p2.y)/2
	return Point(mx,my)


p1=Point(5,10)
p2=Point()
p3=midpoint(p1,p2)
p4=p1.halfway(p2)
print(p1,p2,p1.distanceFromOrigin(),p2.distanceFromOrigin())
print(p3)
print(p4)