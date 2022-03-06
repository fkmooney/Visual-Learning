# https://www.caviar20.com/products/frank-stella-delphine-lithograph-1968

def setup():
    size(600,600)
    background(245)
    translate(-10,-20)
    
    for x in range(21):
        stroke(30)
        strokeWeight(13)
        strokeCap(SQUARE)
        strokeJoin(MITER)
        noFill()
        
        beginShape()
        vertex(x*15+10,650)
        vertex(x*15+10, 0+x*15+20)
        vertex(610-x*15, 0+x*15+20)
        vertex(610-x*15, 650)
        endShape()
        
    #line(250,310,306,310)    
   
    saveFrame("output.png")
    
        
    
