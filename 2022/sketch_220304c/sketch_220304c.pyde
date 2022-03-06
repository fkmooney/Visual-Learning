# https://www.caviar20.com/products/frank-stella-delphine-lithograph-1968

def setup():
    size(600,600)
    background(245)
    translate(-40,30)
    
    for y in range(8):
        stroke(52,170,159)
        strokeWeight(16)
        strokeCap(SQUARE)
        strokeJoin(MITER)
        noFill()
        beginShape()
        vertex(-100,y*20+100)
        vertex(400-(y*35),y*20+100)
        vertex(140-(y*18),550-(y*10))
        endShape()
        
    
    pushMatrix()
    rotate(radians(-60))
    translate(-288,317)
    for y in range(8):
        stroke(140,141,165)
        strokeWeight(16)
        strokeCap(SQUARE)
        strokeJoin(MITER)
        noFill()
        beginShape()
        vertex(-100,y*20+100)
        vertex(400-(y*35),y*20+100)
        vertex(125-(y*18),550-(y*10))
        endShape()
    popMatrix()
    
    noStroke()
    fill(245)
    rect(0,500,650,200)
    triangle(15,255,250,600,0,600)
    
    stroke(30)
    strokeWeight(1)
    #line(416,0,416,600)
    
    saveFrame("output.png")
    
        
    
