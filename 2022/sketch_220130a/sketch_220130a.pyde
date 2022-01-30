from itertools import product

#create coordinates for large grid
grid = product(range(56), #size of grid
                repeat=2) # need two for len and wid

def element(pos, step=12): # step is gap btw elements
    i, j = pos # get coords from grid
    r = random(0,255)
    b = random(0,255)
    g = random(0,255)
    fill(r,b, g)
    square(i * step, j * step,step) 

def setup():
    size(600, 600)
    noStroke()
    map(element, grid) 

def draw():
    stroke(245)
    strokeWeight(24)
    noFill()
    square(0,0,width)
    
def keyPressed():
    saveFrame("output.png")
