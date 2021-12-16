# random composition of two rectagles and two circles overlapping

def setup():
    size(700, 700)
    background(255)
    
    frame_size = 700 # create variable to use below based on frame size above
    
    # doing somethin under setup means its there the whole time
    # it doesn't happen at a particular frame

    # create iterating rectangle
    noStroke() # no border
    
    stripes = 40 # number of stripes
    
    for i in range(0, frame_size, frame_size/stripes):
        fill(random(10,240), random(10,240), random(10,240),10d0)
        rect(i, 0, frame_size/stripes,frame_size)

    

def draw():  
    # need something in here in order to create the save logic below
    x = 100
    
def keyPressed():
    saveFrame('####.png')

    
