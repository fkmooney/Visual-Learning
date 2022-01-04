def setup():
    size(600,600)
    background(245)
0
def draw():    
    
    noStroke()
    pushMatrix()
    tam = 15
    rotate(radians(45))
    translate(-100,-400)
    fill(250,250,0)
    rect(0,400,width*2,height)
    for x in range(tam*2):
        fill(0)
        rect(0,0+x*tam*2,width*2,tam)
    popMatrix()
        
    strokeWeight(200)
    stroke(0)
    noFill()
    circle(width/2,height/2,width+200,)
    
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
