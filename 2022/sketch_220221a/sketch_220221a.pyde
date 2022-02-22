def setup():
    size(600,600)
    background(245)   
    noLoop()

def draw():
    
    fill(155,0,0)
    noStroke()
    
    beginShape()
    vertex(0,100)
    vertex(500,100)
    vertex(0,130)
    vertex(0,100)
    endShape(CLOSE)
    
    beginShape()
    vertex(600,110)
    vertex(500,100)
    vertex(600,80)
    vertex(600,110)
    endShape(CLOSE)
    
    fill(00,0,155,)
    beginShape()
    vertex(0,100)
    vertex(500,100)
    vertex(500,70)
    vertex(0,100)
    endShape(CLOSE)
    
    beginShape()
    vertex(500,100)
    vertex(500,70)
    vertex(600,80)
    vertex(500,100)
    endShape(CLOSE)
        
    saveFrame("output.png")     
