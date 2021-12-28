dimension = 600

def setup():
    size(dimension, dimension)
    background(255, 255, 255)
    noStroke()    
  
def draw():
    step = 50
    shape_size = 1.5 # increase makes shapes smaller    
    # draws a tile
    def tile_draw(x, y, wid, hei):  
        fill(255)
        #strokeWeight(5)
        #square(x, y, wid) # outline of tile, needs strokeweight
                
        circleorsquare = random(1) # random numbers between 0 and 1
        tile_local = random(4)
        if circleorsquare < .5:
            fill(0,0,150)
            if tile_local <= 1:
                circle(x+step/shape_size/2, y+step/shape_size/2, step/shape_size)
            elif tile_local <= 2:
                circle(x+step-(step/shape_size/2), y+step/shape_size/2, step/shape_size)
            elif tile_local <= 3:
                circle(x+step-(step/shape_size/2), y+step-step/shape_size/2, step/shape_size)
            else:
                circle(x+step/shape_size/2, y+step-step/shape_size/2, step/shape_size)                
        else:
            fill(0,150,0)
            if tile_local <= 1:
                square(x, y, step/shape_size)
            elif tile_local <= 2:
                square(x+step-step/shape_size, y, step/shape_size)
            elif tile_local <= 3:
                square(x+step-step/shape_size,y+ step-step/shape_size, step/shape_size) 
            else:
                square(x,y+ step-step/shape_size,step/shape_size)   
                        
    # lays out tiles
    for x in range(0, dimension, step):
        for y in range(0, dimension, step):
            tile_draw(x, y, step, step)
    noLoop() # draws it once
    
def keyPressed():
    saveFrame("output.png") 
