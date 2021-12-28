dimension = 600

def setup():
    size(dimension, dimension)
    background(255, 255, 255)
    #noStroke()    
  
def draw():
    step = 50
    shape_size = 1.5 # increase makes shapes smaller    
    # draws a tile
    def tile_draw(x, y, wid, hei):  
        noFill()
        strokeWeight(15)
        stroke(0,0,255)
        #square(x, y, wid) # outline of tile,
                        
        arcorcross = random(2) # random numbers between 0 and 1
        if arcorcross <=1:
            if random(2) <=1:
                arc(x,y,wid,wid,0,HALF_PI,OPEN)
                arc(x+wid, y+wid, wid, wid, PI, PI+HALF_PI,OPEN)
            else:
                arc(x+wid,y,wid,wid,HALF_PI,PI,OPEN)
                arc(x, y+ wid, wid, wid, PI+HALF_PI,2*PI)                                
        else:
            line(x+step/2,y,x+step/2,y+step)
            line(x,y+step/2,x+step,y+step/2)
                   
    # lays out tiles
    for x in range(0, dimension, step):
        for y in range(0, dimension, step):
            tile_draw(x, y, step, step)
    noLoop() # draws it once
    
def keyPressed():
    saveFrame("output.png") 
