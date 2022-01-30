def setup():
    size(600,600)
    background(205)

def draw():
    iter =60

    for x in range(0,width,iter):
        for y in range(0, height,iter):
            push()
            noStroke()
            fill(255,255,255)
            rx = random(-1,1)
            ry = random(-1,1)
            rect(x+rx, y+ ry,iter+1, iter-3) 
            pop()
    
    noClip()
    filter(BLUR, 6)
    
    noFill()
    stroke(205)
    strokeWeight(10)
    square(0,0,width)
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
    
    
