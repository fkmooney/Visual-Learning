def setup():
    size(600,600)
    background(28,108,131)   
    noLoop()

def draw():

    loosness = 1

    for x in range(0,4,1):
        for y in range(0,4,1):
            stroke(245,145)
            for xx in range(-5,605,5):
                circle(xx+x+random(-loosness,loosness), 
                       50+y+random(-loosness,loosness), 1)
    
    saveFrame("output.png")               
