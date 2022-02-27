def setup():
    size(600,600)
    background(245) 
    
def draw():
    translate(30,0)
    font = createFont("Montserrat-Black.otf", 85)
    textFont(font)
    textSize(40)

    fill(30)
    xx = 185
    yy = 290
    te = "ON THE TIP OF"
    for x in range(-1,2):
            text(te, xx+x, yy+x)
            text(te, xx+x, yy-x)
    fill(131,167,255)
    text(te, xx,yy)
    
    fill(30)
    xx = 155
    yy = 330
    te = "A WAVE"
    for x in range(-1,2):
            text(te, xx+x, yy+x)
            text(te, xx+x, yy-x)
    fill(131,167,255)
    text(te, xx,yy)
    
    fill(245)
    strokeWeight(6)
    strokeCap(SQUARE)
    arc(-75, 100, 620, 670, PI*0.1, PI*0.4, OPEN)
    
    fill(30)
    xx = 32
    yy = 250
    t = "PLACED"
    for x in range(-1,2):
            text(t, xx+x, yy+x)
            text(t, xx+x, yy-x)
    fill(131,167,255)
    text(t, xx,yy)
    
    noLoop()
    saveFrame("output.png")
