# random composition of two rectagles and two circles overlapping

def setup():
    size(700, 700)
    background(255)
    
    frame_size = 700 # create variable to use below based on frame size above
    
    # doing somethin under setup means its there the whole time
    # it doesn't happen at a particular frame

    # create iterating rectangle
    noStroke() # no border
    fill(0,50)
    
    i = 1
    
    x_axis = random(5,frame_size/4)
    y_axis = random(5,frame_size/4)
    
    for i in range(100):
        x = random(10,frame_size-20-(x_axis))
        y = random(10,frame_size-20- (y_axis))
        # draw rectangle using position and l x w
        rect(x, y, x_axis,y_axis)
        i = i+1    
    

def draw():  
    # need something in here in order to create the save logic below
    x = 100
    
def keyPressed():
    saveFrame('####.png')

    
