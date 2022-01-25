# inspired by Athos Bulcão's work

from random import choice

def pattern(d, angle=0):
    rotate(angle)
    h = d / 2
    arc(-h, h, 2 * d, 2 * d, TWO_PI - HALF_PI, TWO_PI)

def setup():
    size(600, 600)
    strokeWeight(5)
    noFill()

def draw():
    background(245)
    tam = 60
    rot_angles = [0, HALF_PI, PI, 3 * HALF_PI]

    for x in range(0, width, tam):
        for y in range(0, height, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                if random(0,5) < 1:
                    stroke(235,0,0)
                else:
                    stroke(30)
                pattern(tam, choice(rot_angles))

    noLoop()

def keyPressed():
    saveFrame("output.png")
