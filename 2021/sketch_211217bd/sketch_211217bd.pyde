
dimension = 600

def setup():
    size(dimension, dimension)
    step = 25
    background(255, 255, 255)
    strokeWeight(3)
    

    def funky_draw(x, y, wid, hei):    
        leftToRight = random(1) # random numbers between 0 and 1
        if leftToRight >= .5:
            line(x, y, x + wid, y + hei)
            
        else:
            line(x +wid, y, x, y + hei)
           

    for x in range(0, dimension, step):
        for y in range(0, dimension, step):
            funky_draw(x, y, step, step)
             
  
def draw():
    b=1
    
def keyPressed():
    saveFrame("##.png") 
    
