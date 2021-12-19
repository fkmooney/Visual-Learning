dimension = 600
curvas = []
step = 20
n = dimension/step - 8 # controls number of lines

def setup():
    size(dimension, dimension) # size of canvas
    background(0) 
    stroke(255, 255, 255)
    strokeWeight(1)

    # create frame   
    beginShape()
    fill(0)
    vertex(0,0)
    vertex(width,0)    
    vertex(width,height)
    vertex(0,height)  
    endShape(CLOSE)  
    
    # iterate 
    for i in range(n):
        
        # makes a  line with fill below it
        beginShape()
        noFill()
        for x in range(width):            
            
            ypoint = i + random(-1, 1) 
            
            distanceToCenter = abs(x - dimension / 2)
            variance = max(dimension / 2 - 50 - distanceToCenter, 0)
            rand = ypoint * variance/60  * -1
            
            vertex(x, (rand + (i*step) + 4 * step)) 
            #i = rand        
     
        vertex(width, height)
        vertex(0,height)
        endShape(CLOSE)

def draw():
    b=1
           
def keyPressed():
        saveFrame("####.png")        
