def setup():
    size(600, 600)
    background(245)
    noStroke()
    fill(20,20,20,230)


def draw():
    translate(35, 35)
    for x in range(0,5):
        for y in range(0,5):
            gap = 106
            adj_amount = 12
            ranx = random(-adj_amount,adj_amount)
            rany = random(-adj_amount,adj_amount)
            square(x*gap + ranx, y*gap + rany, 100)
            
    noLoop()


def keyPressed():
    saveFrame("output.png")
