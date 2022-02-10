# inspired by Brice Marden's Cold Mountain Series, Zen Study 6, (1991)
from itertools import product
from random import choice

def setup():
    size(600, 600)
    background(245)
    strokeWeight(4)

def draw():
    border = 25
    translate(border, border)
    grid_step = 30
    draw_width = width-2*border
    btw_gapx = 90
    btw_gapy = 115
    start_x = -2
    start_y = -2
    
    for x in range(0,6):
        beginShape()
        for y in range(0,5):    
            noFill()
            stroke(random(30,120))
            grid = product(range(4), repeat=2)
            grid_list = [item for item in grid]
            shape_list = grid_list
            grid_len = 12-y*2
                        
            for i in range(grid_len):
            
                if start_x > -1 and start_y > -1:
                    curveVertex(start_x, start_y)
                    start_x = -2
                    start_y = -2
                    
                
                xp, yp = shape_list.pop(int(random(len(shape_list))))
                xpv = xp * grid_step + x * btw_gapx
                ypv = yp * grid_step + y * btw_gapy
                curveVertex(xpv, ypv)
                
                if i == (grid_len-1) and y < 3:
                    start_x, start_y = xpv, ypv                    
        endShape()
    noLoop()
        
def keyPressed():
    saveFrame("output.png")
