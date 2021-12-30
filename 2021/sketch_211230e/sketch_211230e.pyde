# inspired by Athos Bulcão's work

from random import choice

def pattern_1(d, angle=0):
    rotate(angle)
    h = d / 2
    arc(h, 0, d, d, HALF_PI, PI)

def pattern_4(d, angle=0):
    rotate(angle)
    h = d / 2
    arc(-h, h, 2 * d, 2 * d, TWO_PI - HALF_PI, TWO_PI)



patterns = [
    #pattern_1,
    pattern_4,]

def setup():
    size(600, 600)
    noStroke()
    fill(255)


def draw():
    background(0,0,245,3)

    tam = 60
    rot_angles = [0, HALF_PI, PI, 3 * HALF_PI]

    for x in range(0, width, tam):
        for y in range(0, height, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                if random(0,10) < 1:
                    fill(235)
                else:
                    fill(35)
                pattern = choice(patterns)
                pattern(tam, choice(rot_angles))

    noLoop()

def keyPressed():
    saveFrame("output2.png")
