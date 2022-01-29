def setup():
    size(600, 600)
    background(245)
    strokeWeight(20)
    stroke(30)
    noFill()
    
def draw():   
    # create graphics for triangle
    lines = createGraphics(600,600)
    lines.beginDraw()
    lines.background(245)
    lines.strokeWeight(20)
    lines.stroke(30)
    for y in range(5,600, 40):
        lines.line(0,y,600,y)
    lines.endDraw()
    
    # create triangle shape
    maskImage = createGraphics(600,600)
    maskImage.beginDraw()
    maskImage.triangle(width/2,height*1/5, width *4/5, height*3/4, width *1/5,height*3/4)
    maskImage.endDraw()
    
    # paste graphics onto traingle shape
    lines.mask(maskImage)
    
    # background
    for x in range(0,width+1,40):
        line(x,0,x,height)
        
    # show triangle
    image(lines,0,0)        
    noLoop()    

def keyPressed():
    saveFrame("output.png")
