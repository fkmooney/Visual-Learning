from itertools import product

#create coordinates for large grid
grid = product(range(38), #size of grid
                repeat=2) # need two for len and wid


def element(pos, step=15): # step is gap btw elements
    i, j = pos # get coords from grid
    line(i * step, # could iterate over other shapes if you want
         j * step,
         i * step, 
         j * step + random(i * -j / 20.0)) # last digit controls where change occurs

def setup():
    size(600, 600)
    background(245)
    translate(23, 23)
    strokeWeight(5)
    map(element, grid) 

def draw():
    b=1

def keyPressed():
    saveFrame("output.png")
