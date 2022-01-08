def setup():
    size(600, 600)
    strokeWeight(1)

def draw():
    background(245)

    for i, x in enumerate(range(0, width, 10)):
        index = (10 + i) * 0.07
        max_y = int(map(noise(index), 0, 1, 0, height))

        stroke(245)

        for y in range(max_y-500, width, 20):
            fill(random(255), random(255), random(255), random(100,230))
            rect(x, y, 10, 20)
            
    noFill()
    strokeWeight(50)
    square(0,0,width)
    noLoop()


def keyPressed():
    saveFrame("####.png")
