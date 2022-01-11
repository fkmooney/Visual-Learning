# draws a rect with ragged edges

def setup():
    size(600,600)
    background(245)
    
def draw():
    
    noStroke()
    fill(225,30,30,230)
    granularity = 10
    amt = 1
    
    def ragged_rect(xp, yp, wid, hei):
        pushMatrix()
        rotate(radians(random(-10,10)))
        beginShape()
        vertex(xp, yp)
 
        for x in range(xp, xp + wid, granularity):                        
            vertexy = yp  + random(-1,1) * amt
            vertex(x, vertexy)   
    
        vertex(xp+wid, yp)
 
        for x in range(yp, yp+hei, granularity):                      
            vertexy = xp+wid  + random(-1,1) * amt
            vertex(vertexy, x)         
    
        vertex(xp + wid, yp+hei)
 
        for x in range(xp+wid , xp, -granularity):                       
            vertexy = yp+hei  + random(-1,1) * amt
            vertex(x, vertexy)         
    
        vertex(xp, yp+hei)

        for x in range(yp+hei, yp, -granularity):                        
            vertexy = xp  + random(-1,1) * amt
            vertex(vertexy, x)       
    
        vertex(xp, yp)        
        endShape(CLOSE)
        popMatrix() 
              
    ragged_rect(100,100,150,75) 
    ragged_rect(100,200,150,75)  
    ragged_rect(100,300,150,75) 
    ragged_rect(100,400,150,75) 
    
    ragged_rect(300,100,150,75) 
    ragged_rect(300,200,150,75)  
    ragged_rect(300,300,150,75) 
    ragged_rect(300,400,150,75) 
    
    noLoop()
    
    
def keyPressed():
    saveFrame("output.png")
        
