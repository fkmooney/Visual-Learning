def setup():
    size(600,600)
    background(245)
    
    rotate(radians(-45))
    translate(-1000,0)
    
    iter = 4000

    # using a square grid as a starting shape
    # add area to one side of square, which subtracts from opposite site
    # this transforms square to abstract shape
    for x in range(0,iter,110):
        for y in range(0,iter, 60):
            
            x = x+ 50
            
            fill(250,100,100)
            noStroke()
               
            
            beginShape() # repeat last three vertexes to have round shape
            curveVertex(x+8, y-8 ) 
            curveVertex(x+45, y+10 )            
            curveVertex(x+100, y-8 )
            curveVertex(x+100, y+10 )  
            curveVertex(x+75, y+22 ) 
            curveVertex(x+82, y+50 ) 
            curveVertex(x+45, y+35 )
            curveVertex(x-10, y+55 )
            curveVertex(x-15, y+30 )
            curveVertex(x+5, y+22 )
             
            curveVertex(x+8, y-8 ) 
            curveVertex(x+45, y+10 )            
            curveVertex(x+100, y-8 ) 

            endShape(CLOSE)

    saveFrame("output.png")
