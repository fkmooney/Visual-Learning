def setup():
    size(600,600)
    background(245)
    noStroke()
    
    
    
def draw():
    grid = width/5

    for x in range(0,2*width,grid):
        for y in range(0, 2*height, grid):
            fill(255,120,70)
            circle(x,y+grid/2, grid-2)
            
    for x in range(0,width,grid):
        for y in range(0, height, grid):
            switch = random(0,5)
            if switch <= 3:
                fill(50,50,255, 150)
                square(x+1,y+1, grid-2)
    
                
    
    noLoop()
    


def keyPressed():
    saveFrame("output.png")
