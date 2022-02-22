def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB, 360,100,100)
    noLoop()

def draw():
    background(0)


    fill(30)
    circle(300,300,100)

    spotLight(100, 100, 85, 
              260, 300, 800, 
              0, 0, -1, 
              PI/2, 80)

    spotLight(64, 100, 100, 
              300, 300, 800,  # loc
              0, 0, -1, 
              PI*0.2, 180)
    

    # back wall

    cols = 20
    tam = width / cols
    zz=1
    for x in range(cols):
        for y in range(cols):
            fill(200,0,100)
            with pushMatrix():
                translate(tam / 2 + x * tam, tam / 2 + y * tam, -50)
                box(30)
    
