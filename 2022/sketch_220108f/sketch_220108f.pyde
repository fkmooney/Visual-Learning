def setup():
    size(600,600)
    background(245)
    
def draw():
    
    gap = 75
    translate(75,150)
    
    for x in range(0,7):
        for y in range(0,5):
            noStroke()

            fill(243,243,190)
            circle(x * gap, y * gap, 50)
            
    saveFrame("output.png")
    
