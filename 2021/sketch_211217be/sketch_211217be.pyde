dimension = 600
curvas = []
step = 20
n = dimension/step - 8 # controls number of lines

def setup():
    size(dimension, dimension) # size of canvas
    background(0) 
    stroke(255, 255, 255)
    strokeWeight(3)
    
    
    curvas[:] = []
    for i in range(n):
        curvas.append((random(-height/6,height/6),
                  random(-height/6, height/6),
                  random(.33, 1),
                  random(.33, 1),
                  random(.33, 1),))

def draw():
    
    # create frame   
    beginShape()
    fill(0)
    vertex(0,0)
    vertex(width,0)    
    vertex(width,height)
    vertex(0,height)  
    endShape(CLOSE)  
    
    
    # iterate 
    for i, (h, a, f1, f2, f3) in enumerate(curvas):
        
        # makes a curved line with fill below it
        beginShape()
        fill(0)
        for x in range(width):
            ang = x/15. 
            s = sin(ang * f1) + sin(ang * f2) + sin(ang * f3) 
            
            ypoint = (- h + 10 + s/2 * a) / 150
            
            distanceToCenter = abs(x - dimension / 2)
            variance = max(dimension / 2 - 50 - distanceToCenter, 0)
            rand = ypoint * variance / 2 * -1
            
            vertex(x, (rand + (i*step) + 4 * step))
            
        vertex(width,height)
        vertex(0,height)
        endShape(CLOSE)
       
def keyPressed():
        saveFrame("####.png")        
