# inspired by Vera Molnars work: Hommage à Dürer, 400 aiguilles, traversées par un fil
from itertools import product
from random import choice

def setup():
    size(600, 600)
    background(245)
    strokeWeight(1)

def draw():
    border = 75
    translate(border,border)
    grid_step = 30
    draw_width = width-2*border
    btw_gap = 120
    start_x = -2
    start_y = -2
    
    for x in range(0,4):
        for y in range(0,4):    
            noFill()
            grid = product(range(4), repeat=2)
            grid_list = [item for item in grid]
            shape_list = grid_list
            grid_len = len(grid_list)

            beginShape()            
            for i in range(grid_len):
            
                if start_x > -1 and start_y > -1:
                    vertex(start_x, start_y)
                    start_x = -2
                    start_y = -2
                    
                
                xp, yp = shape_list.pop(int(random(len(shape_list))))
                xpv = xp * grid_step + x * btw_gap
                ypv = yp * grid_step + y * btw_gap
                vertex(xpv, ypv)
                
                if i == (grid_len-1) and y < 3:
                    start_x, start_y = xpv, ypv                    
            endShape()
    noLoop()
        
def keyPressed():
    saveFrame("output.png")
    
