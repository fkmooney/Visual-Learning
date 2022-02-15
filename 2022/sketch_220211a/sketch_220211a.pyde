# https://static01.nyt.com/images/2013/07/27/arts/sub-de-maria-obit-2/sub-de-maria-obit-2-articleLarge.jpg?quality=75&auto=webp&disable=upscale
# https://www.metalocus.es/sites/default/files/styles/mopis_news_gallery_first_deskop/public/file-images/ml_walter_de_maria_03_700.jpg?itok=oitpaNKf

def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB, 360,100,100)

def draw():
    background(255,0,95)
    rotateX(radians(-6))
    translate(0, -170,190)

    fill(255,0,95)
    stroke(30)
    strokeWeight(1)

    translate(100,590, 0)    
    for zz in range(0, 50):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(65))
        drawCylinder(10, 70)      
        popMatrix()
        
    translate(80,0, 2000)    
    for zz in range(0, 50):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(-65))
        drawCylinder(10, 70)      
        popMatrix()   

    translate(80,0, 2000)    
    for zz in range(0, 50):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(65))
        drawCylinder(10, 70)      
        popMatrix() 
        
    translate(80,0, 2000)    
    for zz in range(0, 50):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(-65))
        drawCylinder(10, 70)      
        popMatrix() 

    translate(80,0, 2000)    
    for zz in range(0, 50):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(65))
        drawCylinder(10, 70)      
        popMatrix() 
        
    translate(80,0, 2000)    
    for zz in range(0, 50):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(-65))
        drawCylinder(10, 70)      
        popMatrix() 

    noLoop()
    
def drawCylinder(r, h):

    sides = 6
    angle = 360 / sides
    halfHeight = h / 2
    
    # draw top of the tube
    beginShape()
    for i in range(0,sides):
        x = cos( radians( i * angle ) ) * r
        y = sin( radians( i * angle ) ) * r
        vertex( x, y, -halfHeight)
    endShape(CLOSE)

    # draw bottom of the tube
    beginShape()
    for i in range(0, sides):
        x = cos( radians( i * angle ) ) * r
        y = sin( radians( i * angle ) ) * r
        vertex( x, y, halfHeight)
    endShape(CLOSE);
    
    # draw sides
    beginShape(QUAD_STRIP);
    for i in range(0, sides + 1):
        x = cos( radians( i * angle ) ) * r
        y = sin( radians( i * angle ) ) * r
        vertex( x, y, halfHeight)
        vertex( x, y, -halfHeight)    
    endShape(CLOSE);
