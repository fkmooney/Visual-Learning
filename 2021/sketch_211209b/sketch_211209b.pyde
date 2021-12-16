# random composition of two rectagles and two circles overlapping

def setup():
    size(700, 700)
    background(255)
    
    frame_size = 700 # create variable to use below based on frame size above
    
    # doing somethin under setup means its there the whole time
    # it doesn't happen at a particular frame

    # create iterating rectangle
    noStroke() # no border
    fill(176,224,230,50)
    
    i = 1
    
    for i in range(50):
        x = random(10,frame_size)
        y = random(10,frame_size)
        # draw rectangle using position and l x w
        rect(x,y, random(0,frame_size-x),random(0,frame_size-y))
        i = i+1    
    

def draw():  
    # need something in here in order to create the save logic below
    x = 100
    
def keyPressed():
    saveFrame('####.png')

    
