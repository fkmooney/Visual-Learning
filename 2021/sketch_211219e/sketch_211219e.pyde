def setup():
    size(600, 600)
    background(245)
    strokeWeight(1)

def draw():

    def singleline(x, y):
        line(x, y, x, y+200)

    for i in range(5, width, 30):

            translateAmt = i /70 * random(20) 
            rotateAmt = i / 9  
            
            pushMatrix()
            translate(i + translateAmt, 0)
            rotate(radians(rotateAmt))
            singleline(0, 200)
            popMatrix()
            
    noLoop()

def keyPressed():
    saveFrame("output.png")
