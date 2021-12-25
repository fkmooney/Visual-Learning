dimension = 320
finalSize = 10
startSize = dimension
startSteps = 4

def setup():
    size(dimension, dimension) # size of canvas
    background(255) 
    stroke(0)
    strokeWeight(0)
    
    def drawobject(x,y,wid, hei, steps, startSize):
        
        for step in range (1,steps):
             ran1 = random(0,255)
             ran2 = random(0,255)
             ran3 = random(0,255)
             fill(ran1,ran2,ran3)   

             rect(x, y, startSize, startSize)
             startSize = startSize * 2/3
             x = x + (startSize / 4) 
             y = y + startSize * 1/3
             steps = steps - 1 
            

    drawobject(0,0, startSize, startSize,  startSteps, startSize)

def draw():
    b=1
           
def keyPressed():
        saveFrame("####.png")
