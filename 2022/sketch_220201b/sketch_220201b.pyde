def setup():
    size(600,600)
    background(245)
    noStroke()
    
def draw():
    rotate(radians(-45))
    scale(1.3)
    translate(-60,-60)
    
    fill(175,0,0)
    
    
    rect(20,200, 90, 80)
    rect(0,300, 180, 50)
    rect(-5,360, 45, 27)
    rect(65,363, 240, 56)
    rect(-2,430, 75, 60)
    
    rect(-100,320, 30, 10)
    rect(-130,340, 90, 30)
    rect(-70,400, 25, 15)
    
    saveFrame("output.png")
    
    
    
