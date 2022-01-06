from itertools import product
from random import choice

cell_size = 45

def setup():
    global cell_size, cell_half
    size(600, 600)
    cell_half = cell_size / 2

def draw():
    background(245)
    translate(cell_size * 1.2, cell_size * 1.4) # adjust centering
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
    translate(cell_size,0)
    poly_draw()
    translate(cell_size,0)
    poly_draw()  
    translate(cell_size,0)
    poly_draw() 
    translate(cell_size,0)
    poly_draw()  
    translate(cell_size,0)
    poly_draw()  
    translate(cell_size,0)
    poly_draw()  
    translate(cell_size,0)
    poly_draw()  
    translate(cell_size,0)
    poly_draw()  
    translate(cell_size,0)
    poly_draw()  
    popMatrix()

def poly_draw():   
    
    pts = [(random(5), 0),
           (random(5,10), 0), 
           (random(5,10),1),
           (random(5), 1)]
    
    pushStyle()
    strokeWeight(2)  
    stroke(0)
    noFill()
    if len(pts) >= 3:
        beginShape()
        for x, y in pts[::-1]:
            sx = (x + 1) * cell_half * 0.35 # adjust to mess w horz spacing
            sy = (y + 1) * cell_half
            vertex(sx, sy)            
        endShape(CLOSE)

    popStyle()
###################################################
