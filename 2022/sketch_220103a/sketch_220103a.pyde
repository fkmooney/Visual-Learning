def setup():
    background(225)
    rectMode(CENTER)
    size(600,600)
    noStroke()
    
def draw(): 
    pushMatrix()
    translate(width, height/2)
    rotate(radians(45))
    fill(125)
    rect(0,0, width *7/8, height*2)
    popMatrix()
    
    translate(width/2, height/2)
    rotate(radians(45))
    fill(225,100,50)
    rect(0,0, 150, height*2)
        
    fill(0)
    gap = 25
    translate(-width-gap/2,0)
    for x in range(0,width, gap):
        rect(0,0, gap, height*2)
        translate(gap*2,0)
    translate(width/2,0)
    
    noLoop()
    
def keyPressed():
    saveFrame("ouput.png")
