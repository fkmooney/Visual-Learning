def setup():
    size(600, 600)
    background(245)
    strokeWeight(2)
    stroke(255,110,0)
    noFill() 

def draw():

    lines = 7
    granularity = 6
    step = width/lines
    
    for i in range(lines):    
        beginShape()
        for x in range(0, width, granularity):                
            vertexy = i * step + random(-1,1) * 1
            curveVertex(x, vertexy)           
        endShape()   
          
    for i in range(lines):
        beginShape()
        for y in range(0, width, granularity):            
            vertexy = i * step + random(-1,1) * 1
            curveVertex(vertexy, y)            
        endShape()      
    
    # frame
    strokeWeight(153)  
    stroke(245) 
    square(0,0,width)
    
    strokeWeight(65) 
    rect(width/2-2,0,0,height)
    
    noLoop()

def keyPressed():
    saveFrame("output.png")
