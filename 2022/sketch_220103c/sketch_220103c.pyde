def setup():
    background(0)
    size(600,600)
    noStroke()
    rectMode(CENTER)
    
    
def draw():
    count = 8
    wid = width
    color_adj = 1
    for x in range(0, count):
        fill(250* color_adj, 50* color_adj, 75 * color_adj)
        
        square(width/2, width/2, wid)
        wid = wid * .85
        color_adj = color_adj *.7
    
    
    
def keyPressed():
    saveFrame("output.png")
    
    
    
