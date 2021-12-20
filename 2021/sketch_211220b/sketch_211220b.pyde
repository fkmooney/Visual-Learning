dimension = 600
curvas = []
step = 20
n = dimension/step - 8 # controls number of lines
hor_granularity = 15

def setup():
    size(dimension, dimension) # size of canvas
    background(0) 
    stroke(255, 255, 255)
    strokeWeight(1)

    curvas[:] = []
    for i in range(n):
        curvas.append(random(2,6)) # affects height

    # iterate 
    for i, (a) in enumerate(curvas):
        
        # makes a  line 
        beginShape()
        fill(0)
        for x in range(0, width+hor_granularity, hor_granularity): 
            
            ypoint =  a * random(0,1)/7
            
            distanceToCenter = abs(x - dimension / 2)
            variance = max(dimension / 2 - 50 - distanceToCenter, 0)
            rand = ypoint * variance / -2  # last digit calms from edge to center
            
            vertexy = rand + (i*step) + 4 * step
            vertex(x, vertexy)
            
                       
        vertex(width, height)
        vertex(0,height)
        endShape(CLOSE)


def draw():
    b=1
           
def keyPressed():
        saveFrame("####.png") 
