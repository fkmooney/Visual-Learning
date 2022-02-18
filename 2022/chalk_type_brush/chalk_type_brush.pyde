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
    loosness = 5

    if not painting and frameCount > 1:
        line(mouseX,mouseY, mouseX,mouseY)
        painting = True
    elif painting:
        for x in range(0,10,1):
            for y in range(0,10,1):
                stroke(30,145)
                line(mouseX+x+random(-loosness,loosness),
                     mouseY+y+random(-loosness,loosness), 
                     pmouseX+x+random(-loosness,loosness),
                     pmouseY+y+random(-loosness,loosness))
    
 
                
def keyPressed():
    saveFrame("output.png")               
