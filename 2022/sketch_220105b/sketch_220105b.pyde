from itertools import product

#create coordinates for large grid
grid = product(range(56), #size of grid
                repeat=2) # need two for len and wid


def element(pos, step=10): # step is gap btw elements
    i, j = pos # get coords from grid
    circle(i * step, # could iterate over other shapes if you want
         j * step,
         random(0,18)) # last digit controls where change occurs

def setup():
    size(600, 600)
    background(255)
    translate(23, 23)
    noStroke()
    fill(255,210,210)
    map(element, grid) 

def draw():
    b=1

def keyPressed():
    saveFrame("output.png")
