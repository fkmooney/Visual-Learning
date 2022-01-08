from random import choice

def setup():
    size(600, 600)
    background(245)
    noStroke()
    rectMode(CENTER)


def draw():
    RED = color(255,0,0)
    BLACK = color(30)
    colors = [RED, BLACK]
    
    adj_amount = 200
    translate(width/2, height/2)
    for x in range(0,30):
            pushMatrix()
            ranx = random(-adj_amount,adj_amount)
            rany = random(-adj_amount,adj_amount)
            rotate(radians(random(-15,15)))
            fill(255,238)
            rect(ranx,rany, 80,100)
            pincolor = choice(colors)
            fill(pincolor)
            circle(ranx, rany-45,4)
            popMatrix()

    noLoop()

def keyPressed():
    saveFrame("output.png")
