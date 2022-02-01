from itertools import product

def setup():
    size(600, 600)
    colorMode(HSB, 360,100,100)
    stroke(30)
    strokeWeight(0)
    
def draw():
    #create coordinates for large grid
    dim = 8
    grid = product(range(dim), #size of grid
                repeat=2) # need two for len and wid

    def element(pos, step=width/dim+1): # step is gap btw elements
        i, j = pos # get coords from grid
        rand = random(0,64)
        if rand < 11:
            fill(30, 30,15) # black 
        elif rand < 39: 
            fill(30,0,96) # white
        else:  
            hu = random(0,360) # color
            fill(hu, 100, 100)            
        square(i * step, j * step,step) 
        
    map(element, grid)     
    noLoop()

def keyPressed():
    saveFrame("output.png")
