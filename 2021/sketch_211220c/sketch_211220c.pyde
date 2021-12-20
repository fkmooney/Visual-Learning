dimension = 600
curvas = []
step = 20
aThirdOfHeight = dimension/3


def setup():
    size(dimension, dimension) # size of canvas
    background(255) 
    stroke(0)
    strokeWeight(4)
    
    def drawline(x,y,wid, hei, positions):
        
        pushMatrix()
        translate(x +5, y +5)
        rotate(radians(random(-20,20))) # higher abs numbers increases messiness
        for i in range(0, len(positions)):
            line(positions[i]*wid,0, positions[i]*wid, hei)       
        popMatrix()
        
    for y in range(step,dimension-step, step):
        for x in range(step,dimension-step, step):
            if y < aThirdOfHeight:
                drawline(x,y,step,step,[0.5])
            elif y < aThirdOfHeight *2:
                drawline(x,y,step,step,[0.2,0.8])
            else:
               drawline(x,y,step,step,[0.1, 0.5, 0.9])

    
def draw():
    b=1
           
def keyPressed():
        saveFrame("####.png") 
