import itertools
from random import choice

GRID_SIZE = 50
WIDTH, HEIGHT = 600, 600

x_range = range(GRID_SIZE * 2, WIDTH + 1 - GRID_SIZE * 2, GRID_SIZE)
y_range = range(GRID_SIZE * 2, HEIGHT + 1 - GRID_SIZE * 2, GRID_SIZE)
vertex_per_position = {(x, y): 0 for x, y in itertools.product(x_range, y_range)}
MAX_POINTS = 5
MAX_NUM_SHAPES = 5 # can change
SHAPE_POINTS = 3 # can change

def setup():
    size(WIDTH, HEIGHT)
    background(35)
    blendMode(EXCLUSION)

def draw():
    points = []
    num_points = SHAPE_POINTS
    for i in range(num_points):
        if len(vertex_per_position) < num_points:
            noLoop()

        key = choice(vertex_per_position.keys())
        x, y = key
        points.append(PVector(x, y))

        vertex_per_position[key] += 1
        if vertex_per_position[key] == MAX_POINTS:
            vertex_per_position.pop(key)

    if frameCount % 2:
        fill(242)
    else:
        fill(0, 0, 225)

    noStroke()

    beginShape()
    for v in points:
        curveVertex(v.x,  v.y)
    for v in points:
        curveVertex(v.x,  v.y)
    endShape()

    if frameCount == MAX_NUM_SHAPES:
        noLoop()

def keyPressed():
    saveFrame("cover7.png")
