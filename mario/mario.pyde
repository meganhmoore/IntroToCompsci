class Game:
    def __init__(self,w,h,g):
        self.x=0
        self.y=0
        self.w=w
        self.h=h
        self.g=g
        self.gImg=loadImage('platform2.png')
        self.platforms=[]
        self.platforms.append(Platform(100,300,100,20))
        self.platforms.append(Platform(100,400,100,20))
        self.platforms.append(Platform(200,300,100,20))
        self.platforms.append(Platform(300,200,100,20))
        self.platforms.append(Platform(1000,400,100,20))
        self.enemies=[]
        self.enemies.append(Tazmanian(500,300,700,self.g-19,39,self.g,'tazmanian.png','tazmanian.png',6,self.w,self.h))
        self.enemies.append(Tazmanian(200,100,400,200-19,39,self.g,'tazmanian.png','tazmanian.png',6,self.w,self.h))


    def display(self):
        line(0,self.g,self.w, self.g)
        image(self.gImg,0,self.g+50)
        image(self.gImg,0,self.g+30)
        image(self.gImg,0,self.g)
        
        for p in self.platforms:
            p.display()
        for e in self.enemies:
            e.update()
            e.display()
        
    
        
        
class Platform:
    def __init__ (self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.gImg=loadImage('platform2.png')
        
    def display(self):
        #rect(self.x-game.x,self.y-game.y,self.w,self.h)
        image(self.gImg,self.x-game.x,self.y-game.y,self.w,self.h,0,0,self.w,self.h)
        
        
        
        
class Creature:
    def __init__(self,x,y,r,g,rImg,sImg,rF,w,h):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.vx=0
        self.vy=0
        self.dir=1
        self.rImg=loadImage(rImg)
        self.sImg=loadImage(sImg)
        self.w=w
        self.h=h
        self.rF=rF
        self.f=0
        
        
        
    def display(self):
        self.update()
        #ellipse(self.x,self.y,2*self.r, 2*self.r)
        stroke(255,0,0)
        line(self.x-self.r-game.x, self.g-game.y,self.x+self.r-game.x,self.g-game.y)
        stroke(255)
        
        self.f=(self.f+0.1)%self.rF
        if self.vx>0:
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,int(self.f)*self.w,0,int(self.f)*self.w+self.w,self.h)
        elif self.vx<0:
            image(self.rImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,int(self.f)*self.w+self.w,0,int(self.f)*self.w,self.h)
        else:
            if self.dir>0:
                image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h)
            else:
                image(self.sImg,self.x-self.r-game.x,self.y-self.r-game.y,self.w,self.h,self.w,0,0,78)

class Mario(Creature):
    
    def __init__(self,x,y,r,g,rImg,sImg,rF,w,h):
        Creature.__init__(self,x,y,r,g,rImg,sImg,rF,w,h)
        self.Keys={UP:False, LEFT:False, RIGHT:False}
        self.w=60
        self.h=78
        
    def update(self):
        if self.y+self.r<self.g:
            self.vy+=0.1
            self.y+=self.vy
        else:
            self.vy=0
            self.y=self.g-self.r
            
        if self.Keys[RIGHT]:
            self.vx=1
            self.dir=1
        elif self.Keys[LEFT]:
            self.vx=-1
            self.dir=-1
        else:
            self.vx=0
            
        if self.Keys[UP] and self.vy==0:
            self.vy=-5
            self.y+=self.vy
            
        self.x+=self.vx
        
        if self.x-self.r<=0:
            self.x=self.r
        
        if self.x-game.x >= game.w/2:
            game.x+=1
            
        elif game.x>0 and self.vx!=0:
            game.x-=1
        
        for i in range(len(game.enemies)):
            e=game.enemies[i]
            for self.distance(e) <= in self.r+e.r:
                if self.vy>0:
                    e=game.enemies.pop(i)
                    del e
                else:
                    print "Mario Dead"

        
        for p in game.platforms:
            if (self.y+self.r<p.y or self.g==p.y) and p.x<=self.x<=p.x+p.w:#checks if the middle point of marios feet is at the same y point as the brick
                self.g=p.y
                return 
        self.g=game.g
                
        def distance(self,other):
            return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        
class Tazmanian(Creature):
    def __init__(self,x,x1,x2,y,r,g,rImg,sImg,rF,w,h):
        Creature.__init__(self,x,y,r,g,rImg,sImg,rF,w,h)
        self.x1=x1
        self.x2=x2
        self.vx=-1
        self.w=63
        self.h=61
        
        
    def update(self):
        if self.x<self.x1:
            self.vx=1#changing direction of velocity
        elif self.x>self.x2:
            self.vx=-1
            
        self.x+=self.vx
            
            
            
            
game=Game(800,600,500)
mario=Mario(50,100,39,game.g,'marioRun.png','marioStand.png',4,60,78)
def setup():
    size(game.w,game.h)
    background(0)
    stroke(255)
    
def draw():
    background(0)
    game.display()
    mario.display()
    
def keyPressed():
    mario.Keys[keyCode]=True
    
def keyReleased():
    mario.Keys[keyCode]=False
