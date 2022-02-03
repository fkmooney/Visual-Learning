def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB)

def draw():
    background(0)
    lights()
    """spotLight(51, 0, 360, 
              500, 0, 800, 
              -1, 0, 0, 
              PI/2, 0.3)"""
    translate(-20, -50, -600)
    cols = 25
    tam = width / cols
    for zz in range(4*cols):
       for x in range(4*cols):
        for y in range(cols):

            fill(random(0,360), 200, 255)
            with pushMatrix():
                translate(tam / 2 + x * tam, tam / 2 + y * tam, zz * tam)
                if random(0,50) < 3:
                    sphere(random(2,10))
    noLoop()
