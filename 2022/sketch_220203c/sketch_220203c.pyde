def setup():
    size(600,600)
    background(245)
    noStroke()
    fill(11,95,51)
    
def draw():

    beginShape()
    vertex(200,-2)
    vertex(200,300)
    vertex(400,300)
    vertex(400,602)
    
    vertex(420,602)
    vertex(400,300)
    vertex(200,280)
    vertex(220,-2)
    vertex(200,-2)
    endShape(CLOSE)
    
    noLoop()
    saveFrame("output.png")
    
    
