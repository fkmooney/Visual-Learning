def setup():
    size(480, 500)

def draw():
    background(255,125,0)
    stroke(30)
    
    S = float(min(width, height))
    U = 0.0025
    dL = 0.05
    dA = PI/3.0
    P = "fflfflfrfrfrfrfrflfflffrffrflflflflflfrffr"
    
    strokeWeight(10*U)
    scale(S)
    translate(-dL, -dL)
  
    def drawTurtle(path, dL, dA):
        # going to iterate through letters and match to directions defined below
        for i in range(0,42):
            c = path[i] 
         
            if c == 'f':
                line(0, 0, dL, 0)
                translate(dL, 0)               
            elif c == 'r':
                rotate(dA)
            else:
                rotate(-dA)
                
    for k in range(0, 7):
        push()
        rotate(-PI/6.0)
        for i in range(0,7):
            drawTurtle(P, dL, dA)
        pop() 
        translate(0.0, 5*dL)
    
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
