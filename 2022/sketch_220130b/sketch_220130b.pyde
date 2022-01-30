def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB)

def draw():
    background(0)
    translate(12, 22, -200)
    cols = 25
    tam = width / cols
    for zz in range(cols):
       for x in range(cols):
        for y in range(cols):

            fill(random(0,360), 200, 255)
            with pushMatrix():
                translate(tam / 2 + x * tam, tam / 2 + y * tam, zz * tam)
                if random(0,50) < 15:
                    sphere(2)
    noLoop()
