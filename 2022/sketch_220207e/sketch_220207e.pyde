def setup():
    size(600, 600)
    stroke(30)
    background(245)
    noFill()

def draw():
    
    for x in range(0, width, 20):
        for y in range(0, width, 20):
            strokeWeight(0)
            rect(x, y, 20, 20)
            if 80 < x < width-100 and 80 < y < width-100:
                if 4*x+y < 1420:
                    strokeWeight(2)
                else:
                    strokeWeight(1)   
                    
                ran1 = random(-1,1)
                ran2 = random(-1,1)
                circle(x+10+ ran1,y + 10 + ran2,20)
            
    noLoop()
    saveFrame("output.png")
