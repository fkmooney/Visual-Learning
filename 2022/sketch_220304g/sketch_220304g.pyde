# https://www.caviar20.com/products/frank-stella-delphine-lithograph-1968

def setup():
    size(600,600)
    colorMode(HSB,360,100,100)
    background(10,0,95)
    
    for r in range(0,2):
        pushMatrix()
        translate(160,500)
        rotate(radians(60*r-180))
        for x in range(10):
            stroke(60*r+150,50,70)
            strokeWeight(13)
            strokeCap(SQUARE)
            strokeJoin(MITER)
            noFill()
            
            beginShape()
            vertex(x*16-300, 535) # need to play with y coord to ensure 60 degree angels meet evenely
            vertex(0, x*29+16)
            vertex(300-x*16, 535)
            endShape()
        popMatrix()
        
    noStroke()
    fill(10,0,95)
    rect(0,0,600,100)
    triangle(600,0, 390,100, 600,450)
   
    saveFrame("output.png")
    

    
        
    
