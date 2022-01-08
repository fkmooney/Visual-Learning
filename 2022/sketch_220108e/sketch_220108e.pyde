def setup():
    size(600,600)
    
def draw():
    
    background(255)   
    noStroke()
    fill(0,0,255,40)
    circle(200,200,200)
    circle(400,400,250)
    circle(100,450,200)
    circle(500,50,200)
    filter(BLUR,60)
    filter(BLUR,60) 
    filter(BLUR,60)  
    
    stripes = 5
    gap = width/(stripes )
    pushMatrix()
    translate(0,gap*2/4)
    for y in range(0, width, gap):
        fill(250, 250, 190)
        rect(0, y, width, gap/2)
    popMatrix()
    
    # frame
    noFill()
    strokeWeight(20)
    stroke(245)
    square(0,0,width)
            
    saveFrame("output.png")
    
    noLoop()
    
