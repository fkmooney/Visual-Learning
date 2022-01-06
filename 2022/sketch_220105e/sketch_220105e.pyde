from itertools import product

#create coordinates for large grid
grid = product(range(10), #size of grid
                repeat=2) # need two for len and wid


def element(pos, step=57): # step is gap btw elements
    i, j = pos # get coords from grid
    adj_amount = 4
    ranx = random(-adj_amount,adj_amount)
    rany = random(-adj_amount,adj_amount)
    square(i * step +ranx,
         j * step + rany,
         50)


def setup():
    size(600, 600)
    background(245)
    translate(18, 18)
    noStroke()
    fill(250,250,0,150)
    map(element, grid) 

def draw():
    b=1

def keyPressed():
    saveFrame("output.png")
