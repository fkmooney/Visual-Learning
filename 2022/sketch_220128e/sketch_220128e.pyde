def setup():
    size(600,600)
    background(255,225,0)
    stroke(30)
    strokeWeight(5)

def draw():
    
    iter = 6
    translate(-.5 *  (width/iter),0 )
    
    for x in range(iter+2):
        for y in range(0,iter+2): 
            fill(0,0,255)       
            
            line(x * (width/iter),y * (height/iter),
                 (x +.5) * (width/iter), (y-0.4) * (height/iter))
            beginShape()
            vertex((x +.5) * (width/iter), (y-0.4) * (height/iter))
            vertex((x +.5) * (width/iter), (y-0.7) * (height/iter))
            vertex((x +.65) * (width/iter), (y-0.8) * (height/iter))
            vertex((x +.65) * (width/iter), (y-0.95) * (height/iter))
            vertex((x +.5) * (width/iter), (y-1.05) * (height/iter))
            vertex((x +.35) * (width/iter), (y-0.95) * (height/iter))
            vertex((x +.35) * (width/iter), (y-0.8) * (height/iter))
            vertex((x +.5) * (width/iter), (y-0.7) * (height/iter))
            vertex((x +.5) * (width/iter), (y-0.4) * (height/iter))
            endShape(CLOSE)
            
            line((x +.5) * (width/iter), (y-0.4) * (height/iter),
                 (x+1) * (width/iter), y * (height/iter)) 
            
            beginShape()
            vertex((x+1) * (width/iter), y * (height/iter))
            vertex((x+1) * (width/iter), (y+0.35) * (height/iter)) 
            vertex((x+1.15) * (width/iter), (y+0.45) * (height/iter))
            vertex((x+1.15) * (width/iter), (y+0.6) * (height/iter))
            vertex((x+1) * (width/iter), (y+0.7) * (height/iter))
            vertex((x+0.85) * (width/iter), (y+0.6) * (height/iter))
            vertex((x+0.85) * (width/iter), (y+0.45) * (height/iter))         
            vertex((x+1) * (width/iter), (y+0.35) * (height/iter))
            vertex((x+1) * (width/iter), y * (height/iter))             
        
            endShape(CLOSE)    

    noLoop()
    
def keyPressed():
    saveFrame("output.png")
