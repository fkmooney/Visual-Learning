# inspired by Vera Molnars work: Hommage à Dürer, 400 aiguilles, traversées par un fil
from itertools import product
from random import choice

def setup():
    size(600, 600)
    background(245)
    strokeWeight(1)
    stroke(255,150,0)

def draw():
    border = 70
    translate(border,border)
    grid_step = 15
    draw_width = width-2*border
    btw_gap = 60
    
    for x in range(0,8):
        for y in range(0,8):    
            noFill()
            grid = product(range(4), repeat=2)
            grid_list = [item for item in grid]
            shape_list = grid_list
            grid_len = len(grid_list)

            beginShape()            
            for i in range(grid_len):                
                
                xp, yp = shape_list.pop(int(random(len(shape_list))))
                xpv = xp * grid_step + x * btw_gap
                ypv = yp * grid_step + y * btw_gap
                vertex(xpv, ypv)
                               
            endShape()
    noLoop()
        
def keyPressed():
    saveFrame("output.png")
    
