def setup():
    size(600, 600)
    background(255)
    strokeWeight(1)
    randomDisplacement = 10
    rotateMultiplier = 2

    def singleline(x, y):
        line(x, y, x, y+200)

    for i in range(0, width, 30):

            tplusOrMinus = random(0, 10) 
            rplusOrMinus = random(0, 50) 
            translateAmt = i /70 * tplusOrMinus * random(0,2) 
            rotateAmt = i / 9  #+rplusOrMinus #* rotateMultiplier * random(0,1)
            

            pushMatrix()
            translate(i + translateAmt, 0)
            
            print(rotateAmt)
            rotate(radians(rotateAmt))
            singleline(0, 200)
            popMatrix()

def draw():
    b=1

def keyPressed():
    saveFrame("#########.png")
