def setup():
    size(600, 600)
    noStroke()
    rectMode(CENTER) # this helps make rotaion in place easier

def draw():
    background(235)

    tam = 60
    translate(width/2+60,height/2)
    
    fill(210,210,0,130)
    rect(0, 0, 30, height)
    rotate(radians(tam))
    rect(0, 0, 30, height)
    rotate(radians(tam))
    rect(0, 0, 30, height)
    
    fill(0,0,210,130)
    rotate(radians(tam/3))
    rect(0, 0, 30, height)
    rotate(radians(tam))
    rect(0, 0, 30, height)
    rotate(radians(tam))
    rect(0, 0, 30, height)
    
    fill(210,0,0,130)
    rotate(radians(tam/3))
    rect(0, 0, 30, height)
    rotate(radians(tam))
    rect(0, 0, 30, height)
    rotate(radians(tam))
    rect(0, 0, 30, height)


        


 
    noLoop()

def keyPressed():
    saveFrame("output.png")
