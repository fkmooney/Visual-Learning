def setup():
    size(600,600)
    background(245)
    noStroke()

def draw():
    
    iter = 12
    
    # using a square grid as a starting shape
    # add area to one side of square, which subtracts from opposite site
    # this transforms square to abstract shape
    for x in range(iter+1):
        for y in range(iter+1):
            
            if (x+y)%2 == 0:
                fill(100,200,200)
            else:
                fill(30)                
            
            beginShape()
            curveVertex(x * (width/iter),y * (height/iter)) 
            curveVertex(x * (width/iter),y * (height/iter)) 
            
            curveVertex((x +.2) * (width/iter), (y-0.7) * (height/iter))
            curveVertex((x +.7) * (width/iter), (y+0.1) * (height/iter))  
            curveVertex((x+1) * (width/iter), y * (height/iter)) 
            
            curveVertex((x+1) * (width/iter),(y+1) * (height/iter)) 
            curveVertex((x+.7) * (width/iter),(y+1.3) * (height/iter))
            
            curveVertex((x) * (width/iter),(y+1) * (height/iter))
            
            #curveVertex((x -.7) * (width/iter), (y-0.5) * (height/iter)) 
            curveVertex((x -.3) * (width/iter), (y+.3) * (height/iter)) 
            curveVertex(x * (width/iter),y * (height/iter)) 
 
            endShape(CLOSE)

    # uncomment rect to see a reference grid
    for x in range(iter+1):
        for y in range(iter+1):
            
            noFill()
            strokeWeight(1)
            stroke(200,0,0)
            #rect(x * (width/iter), y * (height/iter), width/iter,height/iter)
        
    noFill()
    strokeWeight(5)
    stroke(245)
    square(0,0,width)
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
    
            
