def setup():
    size(600,600)
    background(131,186,240) 
    
def draw():

    stroke(30)
    strokeWeight(10)
    fill(255, 88, 127)
    rect(80,40,400,80)
    fill(131,186,240)
    rect(80,190,400,80)
    fill(255,237,98)
    rect(80,340,400,80)
    
    strokeCap(SQUARE)
    line(80,550,530,340)
    
    fill(255)
    triangle(480,365, 480,420, 360,420)
    
    font = createFont("Montserrat-Black.otf", 85)
    textFont(font)
    fill(30)
    textSize(60)
    text("HIER", 100,102)
    text("NAAR", 100,252)
    text("DAAR", 100,402)

    noLoop()
    saveFrame("output.png")
