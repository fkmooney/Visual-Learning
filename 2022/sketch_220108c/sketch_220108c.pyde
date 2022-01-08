def setup():
    size(600, 600)


def draw():
    background(255)
    
    noStroke()
    fill(0,0,255,250)
    circle(200,200,200)
    circle(400,400,250)
    circle(100,450,200)
    circle(500,50,200)
    filter(BLUR,60)
    filter(BLUR,60) 
    filter(BLUR,60)       

            
    noFill()
    strokeWeight(40)
    stroke(245)
    square(0,0,width)
    strokeWeight(20)
    rect(0,height * 1/5 ,width, height * 1/5)
    rect(0,height * 3/5 ,width, height * 1/5)
    
    noLoop()

def keyPressed():
    saveFrame("output.png")
