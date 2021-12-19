import math
dimension = 600
step = 20

def setup():
    size(dimension, dimension) # size of canvas
    background(255) 
    stroke(0, 0, 0)
    strokeWeight(1)
    squaresize = 60
    randomDisplacement = 100
    rotateMultiplier = 100
    offset = 10

    def square(wid, hei):
        rect(-wid/2, -hei/2, wid, hei)
        noFill()
    
    for i in range(squaresize, dimension-squaresize, squaresize):
        for j in range(squaresize, dimension-squaresize, squaresize):
            
            plusOrMinus = random(-.1, .1) 
            translateAmt = j / 150 * plusOrMinus * random(0,1) * randomDisplacement
            rotateAmt = j / 150 * plusOrMinus * rotateMultiplier * random(0,1)
            print(translateAmt)
                     
            pushMatrix()
            translate(i + translateAmt + offset, j + offset)
            rotate(radians(rotateAmt))
            square(squaresize, squaresize)
            popMatrix()
            
        
def draw():
    b=1
           
def keyPressed():
        saveFrame("####.png")        
