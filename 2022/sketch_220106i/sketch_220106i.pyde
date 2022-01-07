from itertools import product

#create coordinates for large grid
grid = product(range(40), #size of grid
                repeat=2) # need two for len and wid


def element(pos, step=14): # step is gap btw elements
    i, j = pos # get coords from grid
    
    if   j < 13 :
        k = random(0,4) # last digit controls where change occurs
    elif j < 26: 
        k = random(2,7)
    else:
        k = random(4,11)
    
    circle(i * step, j * step, k)


def setup():
    rectMode(CENTER)
    size(600, 600)
    background(245)
    translate(23, 23)
    fill(245)
    strokeWeight(1)
    stroke(255,110,0)
    map(element, grid) 

def draw():
    b=1

def keyPressed():
    saveFrame("output.png")
