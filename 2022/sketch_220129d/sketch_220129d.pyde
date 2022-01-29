def setup():
    size(600,600)
    background(205)

def draw():
    iter =60

    for x in range(0,width,iter):
        for y in range(0, height,iter):
            clip(x,y, iter,iter)
            noStroke()
            fill(255,255,255)
            rnd = random(-3,3)
            square(x+3+ rnd, y+3+ rnd, iter-6) 
    
    filter(BLUR, 7)
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
    
    
