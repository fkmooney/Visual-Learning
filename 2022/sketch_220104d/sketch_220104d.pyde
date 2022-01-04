def setup():
    size(600,600)
    colorMode(HSB,360,100,100,100)
    background(0,0,96.078431)
    noStroke()
    
def draw():

    tam = 60
    translate(tam/2,tam/2)
    for x in range(0, width, tam):        
        for y in range(0, height, tam):
            with pushMatrix():
                translate(x,y)
                fill(0,100,100,40)
                circle(0,-3,(2*x+2*y+600)/tam)

                fill(120,100,100,40)
                circle(-3,3,(2*x+2*y+600)/tam)    
                
                fill(240,100,100,40)
                circle(3,3,(2*x+2*y+600)/tam)
    

    noLoop()
    
def keyPressed():
    saveFrame("output.png")    

    
