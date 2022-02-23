# Leon Polk Smith No.7809, 1978

def setup():
    size(600,600)
    background(225,225,205)
    noLoop()
    
def draw():
    
    stroke(30)
    strokeWeight(100)
    strokeCap(SQUARE)
    line(135,95,135,600)
    line(600-135,600-95,600-135,0)
    line(135,145,600-135,145)
    line(135,600-95-50,600-135,600-95-50)

    noFill()
    stroke(245)
    strokeWeight(300)
    circle(300,300,900)
    
    saveFrame("output.png")
    
    
