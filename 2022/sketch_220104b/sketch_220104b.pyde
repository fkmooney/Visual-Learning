def setup():
    size(600,600)
    background(110,70,200)

def draw():    
    
    noStroke()
    pushMatrix()
    tam = 15
    rotate(radians(-5))
    translate(-100,0)
    for x in range(tam*2):
        fill(245)
        rect(0,0+x*tam*2,width*2,tam)
    popMatrix()
        
    strokeWeight(40)
    stroke(245)
    noFill()
    rect(0,0,width,height)
    
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
