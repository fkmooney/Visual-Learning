from random import choice

def pattern_4(d):
    if random(0,4) <1:
        fill(0,0,225)
    else:
        fill(35)
    triangle(0, d, d, d,0, 0)  

def pattern_5(d):
    if random(0,4) <1:
        fill(0,0,225)
    else:
        fill(35)
    triangle(d,0, d, d, 0, 0)    

def pattern_6(d):
    if random(0,4) <1:
        fill(0,0,225)
    else:
        fill(35)
    triangle(0,0, 0, d, d, 0)

def pattern_7(d):
    fill(240,0,0)
    circle(d/2,d/2,d)

def pattern_8(d):
    if random(0,4) <1:
        fill(0,0,225)
    else:
        fill(35)
    triangle(d,d, d,0, 0, d)

def pattern_9(d): 
    if random(0,4) <1:
        fill(0,0,225)
    else:
        fill(35)
    rect(0, 0, d, d)



patterns = [
    pattern_4,
    pattern_5,
    pattern_6,
    pattern_7,
    pattern_8,
    pattern_9,

]

def setup():
    size(600, 600)
    noStroke()
    fill(245)

def draw():
    background(245)
    tam = 60
    translate(-tam/2, -tam/2)

    for x in range(0, width, tam):
        for y in range(0, height, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                pattern = choice(patterns)
                pattern(tam)

    noLoop()

def keyPressed():
    saveFrame("output2.png")
