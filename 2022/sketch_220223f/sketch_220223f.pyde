from itertools import product


painting = False # dtermines if cursor drawing or not

def mousePressed():
    if mouseButton == LEFT:
        fill(30,145)
        loop()
    if mouseButton == RIGHT:
        fill(245)
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
    loosness = 12

    if not painting and frameCount > 1:
        line(mouseX,mouseY, mouseX,mouseY)
        painting = True
    elif painting:
        for x in range(0,70,1):
            for y in range(0,70,1):
                noStroke()
                circle(mouseX+x+random(-loosness,loosness),
                     mouseY+y+random(-loosness,loosness), 8)
                
def keyPressed():
    saveFrame("output.png")    
