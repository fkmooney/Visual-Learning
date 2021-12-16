# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s247"  # 20180902
OUTPUT = ".png"

curvas = []
n = 3 # controls number of lines

def setup():
    size(1024, 500) # size of canvas
    noStroke()
    blendMode(MULTIPLY)
    
def keyPressed(): # press to generate image and it's saved by pressing 's'
    if key == "s":
        saveFrame("###.png")
    else: 
        curvas[:] = []
        for i in range(n):
            curvas.append((random(-height/6,height/6),
                  random(-height/6, height/6),
                  random(.33, 3),
                  random(.33, 3),
                  random(.33, 3),
                 ))

def draw():
    background(255) # color of background
    translate(0, height/2) # centers lines vertically
    for i, (h, a, f1, f2, f3) in enumerate(curvas):
        if i % 3 == 0:
            fill(0, 150, 200) # color of line 1
        elif i % 3 == 1:
            fill(200, 150, 2025) # color of line 2
        else:
            fill(100, 150, 200)  # color of line 2
        beginShape()
        for x in range(width):
            ang = x/15. # lower number makes more jagged on top
            s = sin(ang * f1) + sin(ang * f2) + sin(ang * f3) 
            vertex(x, - h +10 + s * a)
        for xx in range(width):
            x = width-xx
            ang = x/30. # lower number makes more jagged on bottom
            s = sin(ang * f1)*1.1 + sin(ang * f2)*1.2 + sin(ang * f3)*1.3
            vertex(x, + h  +10 + s * a)
        endShape(CLOSE)
        
