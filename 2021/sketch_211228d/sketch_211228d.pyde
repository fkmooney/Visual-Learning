curves = []
n = 8 # controls number of lines

def setup():
    size(1200, 600) # size of canvas
    noStroke()
    blendMode(MULTIPLY)
    
def keyPressed(): # press to generate image and it's saved by pressing 's'
    if key == "s":
        saveFrame("###.png")
    else: 
        curves[:] = []
        for i in range(n):
            curves.append((random(-height/10,height/10),
                  random(-height/10, height/10),
                  random(.3, 2),
                  random(.3, 2),
                  random(.3, 2),
                 ))

def draw():
    background(255) # color of background
    translate(0, height/n*2) # centers lines vertically 
    for i, (h, a, f1, f2, f3) in enumerate(curves):
        translate(0, height/n/2) # centers lines vertically 
        fill(0, 150, 225) # color of line 1

        beginShape()
        for x in range(width):
            ang = x/60. # lower number makes more jagged on top
            s = sin(ang * f1) + sin(ang * f2) + sin(ang * f3) 
            vertex(x, - h +10 + s * a)
        for xx in range(width):
            x = width-xx
            ang = x/60. # lower number makes more jagged on bottom
            s = sin(ang * f1)*1.1 + sin(ang * f2)*1.2 + sin(ang * f3)*1.3
            vertex(x, + h  +10 + s * a)
        endShape(CLOSE)
