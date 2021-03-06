from random import choice

def pattern_1(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, -h, d, h)
    arc(h, 0, d, d, HALF_PI, PI)

def pattern_2(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, -h, h, d)

def pattern_3(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(-h, -h, -h, h, h, h)

def pattern_4(d, angle=0):
    rotate(angle)
    h = d / 2
    arc(-h, h, 2 * d, 2 * d, TWO_PI - HALF_PI, TWO_PI)

def pattern_5(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, 0, d, h)
    triangle(-h, 0, 0, 0, 0, -h)

def pattern_6(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(0, 0, 0, h, -h, h)
    triangle(0, 0, 0, -h, h, -h)

def pattern_7(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(0, 0, h, h)
    triangle(0, 0, h, 0, h, -h)

def pattern_8(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(-h, -h, 0, -h, -h, 0)
    triangle(h, h, h, 0, 0, h)

def pattern_9(d, angle=0):
    rotate(angle)
    h = d / 2
    rect(-h, -h, h, h)
    rect(0, 0, h, h)

def pattern_10(d, angle=0):
    rotate(angle)
    h = d / 2
    triangle(0, 0, h, 0, 0, h)
    arc(0, 0, d, d, HALF_PI, PI)
    rotate(PI)
    triangle(0, 0, h, 0, 0, h)
    arc(0, 0, d, d, HALF_PI, PI)


patterns = [
    pattern_1,
    pattern_2,
    pattern_3,
    pattern_4,
    pattern_5,
    pattern_6,
    pattern_7,
    pattern_8,
    pattern_9,
    pattern_10,
]

def setup():
    size(600, 600)
    noStroke()
    fill(245)


def draw():
    background(250)

    tam = 60
    rot_angles = [0, HALF_PI, PI, 3 * HALF_PI]

    for x in range(0, width, tam):
        for y in range(0, height, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                fill(35)
                pattern = choice(patterns)
                #pattern = patterns[-1]
                pattern(tam, choice(rot_angles))

    noLoop()

def keyPressed():
    saveFrame("output2.png")
