from random import choice

CELL_SIZE = 10
CELL_SPACING = 25
ROW_SIZE = CELL_SIZE + CELL_SPACING
GRID_RANGE = range((600 + ROW_SIZE) / ROW_SIZE)

def setup():
    size(600, 600)
    noStroke()        
    
def draw():
    background(245)
    translate(CELL_SPACING/2, CELL_SPACING/2)
    d = CELL_SIZE
    triangles_comb = [
        (0, 0, 0, d, d, d),
        (0, 0, d, 0, d, d),
        (0, d, d, 0, d, d),
        (0, d, d, 0, 0, 0),]
                
    for i in GRID_RANGE:
        for j in GRID_RANGE:
            with pushMatrix():
                translate(i * ROW_SIZE, j * ROW_SIZE)
                prob = noise(i, j, 1)              
                x1, y1, x2, y2, x3, y3 = choice(triangles_comb)
                 
                if prob > 0.32:
                    fill(30)
                elif prob > .20:    
                    fill(255,155,0)
                else:
                    fill(255,30,30)      
                            
                triangle(x1, y1, x2, y2, x3, y3)
    noLoop()
                  
def keyPressed():
    saveFrame("output.png")
