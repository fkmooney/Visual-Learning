# based on Sherrie Levine's After Duchamp From Meltdown 1989

def setup():
    size(600,600)
    background(245)
    
def draw():
    noStroke()
    # row 1
    fill(227,211,192)
    square(0,0,width/3)
    fill(242,202,152)
    square(width/3,0,width/3)
    fill(192,226,227)
    square(width*2/3,0,width/3)
    # row 2
    fill(207,209,209)
    square(0,width/3,width/3)
    fill(247,225,167)
    square(width/3,width/3,width/3)
    fill(85,86,129)
    square(width*2/3,width/3,width/3)    
    # row 3
    fill(85,104,129)
    square(0,width*2/3,width/3)
    fill(247,230,145)
    square(width/3,width*2/3,width/3)
    fill(57,59,90)
    square(width*2/3,width*2/3,width/3)
    
    noFill()
    stroke(245)
    strokeWeight(30)
    square(0,0,width)
    
def keyPressed():
    saveFrame("output.png")

    
    
