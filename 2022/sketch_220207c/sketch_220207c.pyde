# http://artobserved.com/2012/01/london-donald-judd-working-papers-donald-judd-drawings-1963-93-at-spruth-magers-through-february-8-2012/

def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    background(245)
    fill(245)
    stroke(30)

def draw():

    rotateY(radians(20))
    translate(250,75,200)
    
    for y in range(50,550,50):
        translate(0,40,0)      
        box(100,20,77)

    noLoop()

    
