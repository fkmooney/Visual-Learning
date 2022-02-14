# https://static01.nyt.com/images/2013/07/27/arts/sub-de-maria-obit-2/sub-de-maria-obit-2-articleLarge.jpg?quality=75&auto=webp&disable=upscale
# https://www.metalocus.es/sites/default/files/styles/mopis_news_gallery_first_deskop/public/file-images/ml_walter_de_maria_03_700.jpg?itok=oitpaNKf

def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB, 360,100,100)

def draw():
    background(255,0,95)
    lights()
    ambientLight(300, 0, 35)
    #rotateX(radians(-15))
    translate(0, -140,150)

    """spotLight(300, 0, 35, 
              300, 10, 100, 
              0, 1, -1, 
              PI*1, .01)"""

    fill(255,0,95)
    stroke(30)
    strokeWeight(1)

    beginShape() # bottom
    vertex(0, 600, -1200)
    vertex(600, 600, -1200)
    vertex(600, 600, 200)
    vertex(0,  600, 200, )
    vertex(0, 600, -1200)
    endShape()
    
    fill(255,0,95)

    beginShape() # left
    vertex(0, 0, 0)
    vertex(0, 0, -1200)
    vertex(0, 600, -1200)
    vertex(0, 600, 0)
    vertex(0, 0, 0)
    endShape()    

    beginShape() # right
    vertex(600, 0, -1200)
    vertex(600, 0, 0)
    vertex(600, 600, 0)
    vertex(600, 600, -1200)
    vertex(600, 0, -1200)
    endShape()     

    beginShape() # top
    vertex(0, 250, 200)
    vertex(600, 250, 200)
    vertex(600, 250, -1200, )
    vertex(0,  250, -1200)
    vertex(0, 250,  200)
    endShape()

    fill(255,0,60)
    beginShape() # back
    vertex(0, 0, -1200)
    vertex(600, 0, -1200)
    vertex(600, 600, -1200)
    vertex(0, 600, -1200)
    vertex(0, 0,  -1200)
    endShape()
    
    fill(255,0,95)
    translate(100,590, 0)    
    for zz in range(0, 25):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(65))
        drawCylinder(10, 70)      
        popMatrix()
        
    translate(80,0, 1000)    
    for zz in range(0, 25):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(-65))
        drawCylinder(10, 70)      
        popMatrix()   

    translate(80,0, 1000)    
    for zz in range(0, 25):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(65))
        drawCylinder(10, 70)      
        popMatrix() 
        
    translate(80,0, 1000)    
    for zz in range(0, 25):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(-65))
        drawCylinder(10, 70)      
        popMatrix() 

    translate(80,0, 1000)    
    for zz in range(0, 25):
        translate(0, 0, -40)
        pushMatrix()
        rotateY(radians(65))
        drawCylinder(10, 70)      
        popMatrix() 
        
    translate(80,0, 1000)    
    for zz in range(0, 25):
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
    fill(255,0,95)
    
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
