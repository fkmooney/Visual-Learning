from itertools import product
painting = False # dtermines if cursor drawing or not

def mousePressed():
    if mouseButton == LEFT:
        loop()

def mouseReleased():
    noLoop()
    global painting
    painting = False

def setup():
    size(600,600)
    background(245)   
    noLoop()

def draw():

    global painting
    loosness = 2
    nodes = 20
    alph = 240

    if not painting and frameCount > 1:
        line(mouseX, mouseY, mouseX,mouseY)
        painting = True
    elif painting:
        for x in range(0,nodes,1):
            for y in range(0,nodes,1):
                fill(30,alph)
                noStroke()
                
                for yy in range(100,580,5):
                    for xx in range(8,300,10):
                        circle(xx+x+random(-loosness,loosness),
                            yy+y+random(-loosness,loosness), 3)
                
                for yy in range(7,500,5):
                    for xx in range(300,580,5):
                        circle(xx+x+random(-loosness,loosness),
                            yy+y+random(-loosness,loosness), 3)
                                
def keyPressed():
    saveFrame("output.png")               
