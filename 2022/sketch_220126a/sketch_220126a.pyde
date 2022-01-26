def setup():
    size(600, 600)
    background(245)
    
def draw():
    bulk = 200
    strokeWeight(100)
    strokeCap(SQUARE)
    strokeJoin(MITER)    
    stroke(30)
    
    def vert(x,y):
        x = x + random(5, 100)
        mlt = 1 if random(0,10) < 5 else -1
        y = y + mlt * random(5, 100)
        x = x if bulk<x<width-bulk else random(bulk, width-bulk)
        y = y if bulk<y<height-bulk else random(bulk, height-bulk)
        vertex(x, y)
        
    noFill()
    beginShape()
    
    x = -50
    y = random(30, height -30)
    vertex(x, y)
    
    vert(x,y)
    vert(x,y)
    vert(x,y)
    vert(x,y)
    vert(x,y)
    vert(x,y)

    endShape()
    noLoop()
        
def keyPressed():
    saveFrame("output.png")
