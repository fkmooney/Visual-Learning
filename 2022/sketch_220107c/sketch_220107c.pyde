
def setup():
    size(600, 600)
    background(245)
    strokeWeight(2)
    stroke(255,110,0)
    noFill() 

def draw():

    for i in range(50):
        step = 15
        granularity = 3  
    
        beginShape()
        for x in range(0, width, granularity):            
                
            vertexy = i * step + random(-1,1) * 2
            curveVertex(x, vertexy)
            
        endShape()   
          
    strokeWeight(20)  
    stroke(245) 
    square(0,0,width)
    
    noLoop()

def keyPressed():
    saveFrame("output.png")
