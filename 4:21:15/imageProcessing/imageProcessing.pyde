img=loadImage('test.jpg')

def setup():
    size(800,600)
    background(0)
    
def draw():
    image(img,10,10)
    image(img,10,220,70,70)
    image(img,10,300,160,200,160,0,320,200)
    image(img,200,300,70,70,160,0,320,200)
