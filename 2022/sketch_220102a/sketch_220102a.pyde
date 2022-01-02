
def pattern_4(d):
    h = d / 2
    circle(h,h,d-5)

def setup():
    size(600, 600)
    noStroke()
    fill(255)

def draw():
    background(0)

    tam = 60
    rotate(radians(-90))
    translate(-tam, -tam)
    translate(-width,0)
    for x in range(0, width+tam, tam):
        for y in range(0, height+tam, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                fill(0,205,0)
                pattern_4(tam)

    translate(tam, tam)
    for x in range(0, width-tam, tam):
        for y in range(0, height-tam-x, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                fill(225)
                pattern_4(tam)    
    noLoop()

def keyPressed():
    saveFrame("output.png")
