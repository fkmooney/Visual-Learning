#genuary prompt: 500 lines

points = [] 

def setup():
    size(900, 900, P3D)
    points.append(PVector.random3D() * 128)
    while len(points) < 200: # prompt is here for density
        p = PVector.random3D() * 128
        if 127 < PVector.dist(p, points[-1]) < 128:
            points.append(p)
     
def draw():
    background(255)
    strokeWeight(1)
    translate(width / 2, height / 2, 128)
    scale(2)
    #rotateY(frameCount / 200.0) # uncomment to rotate
    for i, (xa, ya, za) in enumerate(points):
        xb, yb, zb = points[i - 1]
        #stroke(128 + xa, 128 + ya, 128 + za) # this makes color of lines random
        stroke(0, 125, 125) # use to choose single color fo all lines
        # below modifies line construction
        #line(xa, ya, za, xb, yb, zb) # confines to sphere
        #line(xa, ya, za, xb, .5 * yb, zb) # messier sphere
        #line(xa, 1.5 * ya, za, xb, .3 * yb, zb) # more messy
        line(xa, ya, za, 10 * xb, yb, zb) # horizontal mess
        #line(xa, ya, za, xb, yb, 10* zb) # like a close up
        
def keyPressed():
    saveFrame('###.png')     
        
              
