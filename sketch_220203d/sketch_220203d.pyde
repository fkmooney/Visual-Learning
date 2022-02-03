def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB)

def draw():
    background(0)

    spotLight(51, 0, 360, 
              700, 0, 800, 
              -1, 0, 0, 
              PI/2, 0.3)
    translate(200, 15, -900)
    rotateY(radians(-45))
    cols = 15
    tam = width / cols
    for zz in range(cols):
       for x in range(cols):
        for y in range(cols):

            fill(random(200,250), 200, 255)
            with pushMatrix():
                translate(tam / 2 + x * tam, tam / 2 + y * tam, zz * tam)
                box(25)
    noLoop()
