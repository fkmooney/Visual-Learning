def setup():
    blendMode(ADD) # this allows blending to go to balck or white (use MULTIPLY)
    size(600,600)
    
    background(0)
    noStroke()
    
def draw():

    tam = 60
    translate(tam/2,tam/2)
    for x in range(0, width, tam):        
        for y in range(0, height, tam):
            with pushMatrix():
                translate(x,y)
                fill(255,0,0,220)
                circle(0,-3,(2*x+2*y+600)/tam)

                fill(0,255,0,220)
                circle(-3,3,(2*x+2*y+600)/tam)    
                
                fill(0,0,255,220)
                circle(3,3,(2*x+2*y+600)/tam)
    

    noLoop()
    
def keyPressed():
    saveFrame("output.png")    

    
