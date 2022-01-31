def setup():
    size(600,600)
    background(0)
    
def draw():
    img = loadImage("baltimore_penn.jpg")
    tint(200)
    image(img, 0, height/4, width, height*3/4)
    
    font = createFont("Helvetica-Bold.ttf", 95)
    textFont(font)
    fill(245,150)
    text("HUMANISM", 49, 280)
    text("IS", 265, 360)
    text("OBSOLETE", 49, 445)

    noLoop()
    
def keyPressed():
    saveFrame("ouput.png")
