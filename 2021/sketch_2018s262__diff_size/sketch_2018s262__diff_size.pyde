# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s262"  # 20180917
OUTPUT = ".png"

def setup():
    size(900, 900)
    noStroke()
    rectMode(CENTER)
    blendMode(MULTIPLY)
    
def draw():
    background(255)
    fill(253, 110, 0) # color of circles
    grid(x=width/2, y=height/2,
         order=5, spacing=138,
         function=ellipse, w=115)
    fill(255, 240, 0) # color of square, color is in rbg decimal code
    grid(x=width/2, y=height/2,
         order=7, spacing=100,
         function=rect, w=66)

def grid(x, y, order, spacing, function, w):
    with pushMatrix():
        translate(x - order * spacing / 2, y - order * spacing / 2)
        for i in range(order):
            for j in range(order):
                function(spacing/2 + i * spacing, spacing/2 + j * spacing, w, w) 

def keyPressed(): # press to generate image and it's saved by pressing 's'
    if key == "s":
        saveFrame("####.png")
