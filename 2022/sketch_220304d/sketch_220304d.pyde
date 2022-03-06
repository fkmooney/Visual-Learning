# https://www.caviar20.com/products/frank-stella-delphine-lithograph-1968

def setup():
    size(600,600)
    background(245)
    translate(-2,-10)
    
    for x in range(25):
        stroke(30)
        strokeWeight(13)
        strokeCap(SQUARE)
        strokeJoin(MITER)
        noFill()
        
        beginShape()
        vertex(x*15+10,0)
        vertex(x*15+10, 300-x*15+10)
        vertex(x*15+300, 300-x*15+10)
        vertex(x*15+300, 300+x*15+10)
        vertex(x*15+10, 300+x*15+10)
        vertex(x*15+10, 650)
        endShape()
        
    line(250,310,306,310)    
   
    saveFrame("output.png")
    
        
    
