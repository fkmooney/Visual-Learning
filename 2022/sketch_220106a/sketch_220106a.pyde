from itertools import product

#create coordinates for large grid
grid = product(range(12), # number of grid nodes
                repeat=4) # need two for len and wid


def element(pos, step=50): # step is gap btw elements
    i, j, k, l = pos # get coords from grid
    switch = random(0,500) # increase to reduce number of lines
    if switch <2:
        line(i * step, 
            j * step,
            k * step, 
            l * step ) 

def setup():
    size(600, 600)
    background(245)
    translate(23, 23)
    strokeWeight(2)
    map(element, grid) 

def draw():

    noLoop()

def keyPressed():
    saveFrame("output.png")
