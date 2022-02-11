def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB, 360,100,100)

def draw():
    background(0)
    translate(0,0,-100)

    spotLight(300, 100, 35, 
              200, 300, 800, 
              0, 0, -1, 
              PI/2, 10)

    spotLight(100, 100, 35, 
              400, 300, 800, 
              0, 0, -1, 
              PI/2, 10)
    
    spotLight(200, 100, 35, 
              300, 300, 800, 
              0, 0, -1, 
              PI/2, .01)  
    
     
    spotLight(200, 100, 85, 
              300, 300, -200, 
              0, 0, -1, 
              PI/2, .01) 
    

    # back wall
    cols = 20
    tam = width / cols
    zz=1
    for x in range(cols):
        for y in range(cols):
            fill(200,0,100)
            with pushMatrix():
                translate(tam / 2 + x * tam, tam / 2 + y * tam, zz * tam)
                box(30)
    
    noFill()
    stroke(40,0,95)
    strokeWeight(300)
    beginShape()
    vertex(-100, 50, 100,)
    vertex(700, 50, 100)
    vertex(700, 550, 100)
    vertex(-100,  550, 100)
    vertex(-100, 50, 100)
    endShape(CLOSE)
    
    noLoop()
