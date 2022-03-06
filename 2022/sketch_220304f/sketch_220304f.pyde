# https://www.caviar20.com/products/frank-stella-delphine-lithograph-1968

def setup():
    size(600,600)
    colorMode(HSB,360,100,100)
    background(10,0,95)
    
    for r in range(0,6):
        pushMatrix()
        translate(300,300)
        rotate(radians(60*r))
        for x in range(10):
            stroke(60*r+30,50,100)
            strokeWeight(13)
            strokeCap(SQUARE)
            strokeJoin(MITER)
            noFill()
            
            beginShape()
            vertex(x*16-300, 535) # need to play with y coord to ensure 60 degree angels meet evenely
            vertex(0, x*29+14)
            vertex(300-x*16, 535)
            endShape()
        popMatrix()
   
    saveFrame("output.png")
    

    
        
    
