def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB, 360,100,100)
    noLoop()

def draw():
    background(245)

    spotLight(200, 100, 75, 
              100, 300, 800, 
              0, 0, -1, 
              PI/2, 10)
    
    spotLight(64, 100, 65, 
              350, 150, 800, 
              0, 0, -1, 
              PI/2, 20)

    spotLight(8, 100, 65, 
              500, 350, 800,  # loc
              0, 0, -1, 
              PI*0.2, 10)
    
    # back wall
    cols = 20
    tam = width / cols
    zz=1
    for x in range(cols):
        for y in range(cols):
            fill(200,0,100)
            with pushMatrix():
                translate(tam / 2 + x * tam, tam / 2 + y * tam, -30)
                box(30)
    
