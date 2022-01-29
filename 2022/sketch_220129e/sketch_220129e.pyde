def setup():
    size(600,600)
    background(245)
    noStroke()
    
def draw():
    iter =3
    for x in range(0,width,width/iter):
        for y in range(0, height,height/iter):
            rand = random(5,30)
            fill(rand)
            square(x, y, width/iter) 
    
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
    
    
