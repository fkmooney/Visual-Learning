from itertools import product
from random import choice

ORDER = 10
cell_size = 45

def setup():
    global cell_size, cell_half
    size(600, 600)
    cell_half = cell_size / 2

def draw():
    background(245)
    translate(cell_size * -0.3, cell_size * -0.6 ) # adjust centering
    draw_line()
    
    for x in range(9):
      translate(0, cell_size)  
      draw_line()
    
    noLoop()
    
def keyPressed():
    saveFrame("output3.png")
    
###########################################
def draw_line():         
    pushMatrix()
    poly_draw()
    translate(2*cell_size,0)
    poly_draw()
    translate(2*cell_size,0)
    poly_draw()  
    translate(2*cell_size,0)
    poly_draw() 
    translate(2*cell_size,0)
    poly_draw()  
    popMatrix()

def poly_draw():   
    grid = product(range(8), range(2))# list of possible points 
    pts = [choice(list(grid)), choice(list(grid)), choice(list(grid)),
       choice(list(grid)), choice(list(grid)), choice(list(grid))]
    
    pushStyle()
    strokeWeight(3)  
    noFill()
    if len(pts) >= 3:
        beginShape()
        for x, y in pts[::-1]:
            stroke(0)
            sx = (x + ORDER / 2) * cell_half * 0.7 # adjust to mess w horz spacing
            sy = (y + ORDER / 2) * cell_half
            vertex(sx, sy)            
        endShape(CLOSE)

    elif len(pts) == 2:
        stroke(128)
        beginShape(LINES)
        for x, y in pts:
            sx = (x + ORDER / 2) * cell_half/2
            sy = (y + ORDER / 2) * cell_half
            vertex(sx, sy)
        endShape()
    popStyle()
###################################################
