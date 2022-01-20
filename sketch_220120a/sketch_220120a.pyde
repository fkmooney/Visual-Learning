from itertools import product
from random import sample

points, white_lines = [], []
margin = 100

def setup():
    size(600, 600)
    create_points()
    
    
def create_points():
    points[:] = []
    white_lines[:] = []
    grid = list(product(range(margin, width, margin), repeat=2))
    points.extend(sample(grid, 16)) # last digit controls bend amount
    for p in points:
        for other in reversed(points):
            if p is other: 
                break
            xa, ya = p
            xb, yb = other
            if xa == xb or ya == yb:
                white_lines.append((xa, ya, xb, yb))

def draw():
    background(0)                       
    stroke(0)
    strokeWeight(3)
    fill(255,255,0,)
    beginShape()
    for x, y in points:
        vertex(x, y)
    endShape(CLOSE)
            
def keyPressed():
    saveFrame("output.png")
