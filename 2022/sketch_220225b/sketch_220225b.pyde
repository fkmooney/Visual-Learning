# joan miro the gold of the azure


def setup():
    background(255,245,50)
    size(600,600)
    noLoop()
    
def draw():
    noStroke()
    fill(30)
        
    polygon(100,500, 70, 6,8)
    polygon(310,500, 20, 6, 2)
    polygon(400,480, 30, 6, 3)
    polygon(550,550, 25, 6, 2)
    polygon(550,200, 10, 6, 2)
    polygon(540,300, 20, 6, 2)
    polygon(110,320, 15, 6, 2)
    polygon(510,400, 15, 6, 2)
    polygon(400,80, 10, 6, 2)
    polygon(50,230, 5, 6, 1)
    polygon(490,570, 5, 6, 1)
    fill(235,10,10)
    polygon(130,180, 15, 6, 2)
    fill(10,10,235)
    polygon(380,290, 115, 6, 10)
    
    stroke(30)
    crosses(500,80, 60, 8, 1)
    crosses(230,120, 100, 6, 1)
    crosses(270,420, 25, 11, 1)
    
    line(100,500, 110,320)
    line(550,200, 540,300,)
    
    fill(30)
    beginShape();
    curveVertex(340, 270)
    curveVertex(340, 270)
    
    curveVertex(260, 300)
    curveVertex(190, 400)
    curveVertex(290, 580)
    curveVertex(440, 550)
    
    curveVertex(510, 420)
    
    curveVertex(440, 520)
    curveVertex(290, 560)
    curveVertex(230, 450)
    curveVertex(210, 400)
    curveVertex(240, 340)
    
    curveVertex(340, 270)
    curveVertex(340, 270)
    endShape(CLOSE)
    
def polygon(x, y, radius, npoints, rand):
    angle = TWO_PI / npoints
    beginShape()
    for a in range(0, 9): 
        sx = x + cos(a) * radius
        sy = y + sin(a) * radius
        curveVertex(sx+random(-rand,rand), sy+random(-rand,rand))
    endShape(CLOSE)
 
def crosses(x, y, radius, npoints, rand):
    angle = TWO_PI / npoints
    beginShape()
    for a in range(0, npoints): 
        sx = x + cos(a) * radius
        sy = y + sin(a) * radius
        line(x,y,sx+random(-rand,rand), sy+random(-rand,rand))
    endShape(CLOSE)
    
def keyPressed():
    saveFrame("output.png")
