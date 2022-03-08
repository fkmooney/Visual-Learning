def setup():
    size(600,600)
    background(245)
    
    rotate(radians(-45))
    translate(-1000,0)
    
    iter = 4000
    col_count = 0

    # using a square grid as a starting shape
    # add area to one side of square, which subtracts from opposite site
    # this transforms square to abstract shape
    for x in range(0,iter,110):
        col_count = col_count + 1
        for y in range(0,iter, 60):
            
            if col_count == 0:
                stroke(250,100,100)
                col_count = col_count + 1
            else:
                stroke(150,100,250)
                col_count = col_count - 1
            strokeWeight(10)
            noFill()
            
            x = x+ 40 # shifts position 
            
            beginShape() # repeat last three vertexes to have round shape

            vertex(x+45, y+10 )            
            vertex(x+100, y-6 )
            vertex(x+75, y+22 ) 
            vertex(x+85, y+50 ) 
            vertex(x+45, y+35 )
            vertex(x+5, y+22 )
     
            endShape(CLOSE)

    saveFrame("output.png")
