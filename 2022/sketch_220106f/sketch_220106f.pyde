def setup():
    size(600, 600)
    frameRate(10)
    strokeWeight(5)


def draw():
    background(245)

    for i, x in enumerate(range(0, width, 10)):
        index = (frameCount + i) * 0.07
        max_y = int(map(noise(index), 0, 1, 0, height))

        # top
        stroke(30)
        for y in range(0, max_y, 10):
            line(x, y, x + 10, y)

        # bottom
        stroke(30)
        for y in range(max_y, width, 10):
            line(x+3, y, x+3, y + 10)


def keyPressed():
    saveFrame("####.png")
