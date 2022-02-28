from random import choice

def setup():
    background(245)
    size(600,600)
    
    myImage = loadImage("input.png")
    myImage.resize(600,600)
    image(myImage, 0, 0)
    loadPixels()
    
    pg = createGraphics(600,600)
    pg.beginDraw()
    pg.background(250)
    
    for x in range(0,600,3):
        for y in range(0,600,3):
            c = get(x, y)
            bri = brightness(c)
            ch = [-1,1]
            pg.stroke(bri*1.5)
            pg.strokeWeight(1)
            pg.line(x,y,x+choice(ch), y+choice(ch))
            
    pg.endDraw()
    image(pg,0,0)
    
    stroke(245)
    strokeWeight(20)
    noFill()
    square(0,0,600)
            
    saveFrame("output.png")

            
        

    
