def setup():
    size(600, 600) # size of canvas
    background(245) 
    stroke(0, 0, 0)
    strokeWeight(1)
    noFill()
              
def draw(): 
    #translate(-50,-50)  
    squaresize = 50
    randomDisplacement = .2
    rotateMultiplier = .3

    for i in range(squaresize, width-squaresize, squaresize):
        for j in range(squaresize, height-squaresize, squaresize):
            
            plusOrMinus = random(-.1, .1) 
            plusOrMinus1 = random(-.1, .1)
            translateAmt = j * plusOrMinus * randomDisplacement
            rotateAmt = j * plusOrMinus1 * rotateMultiplier 
                     
            pushMatrix()
            translate(i + translateAmt, j)
            rotate(radians(rotateAmt))
            square(0, 0, squaresize)
            popMatrix()
    noLoop() 
                           
def keyPressed():
        saveFrame("output.png") 
