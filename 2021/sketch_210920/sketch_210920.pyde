axiom = 'X'
rules = {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'S',  
    'S': 'SF'    
    }
step = 12
angle = 30   # angle in degrees
iterations = 6

def setup():
    global result
    size(1000, 900, P3D)
    strokeWeight(1)
    starting_phrase = axiom
    for _ in range(iterations):
        result = ''
        for symbol in starting_phrase:
            replacement = rules.get(symbol, symbol)
            result = result + replacement
        #print(starting_phrase, result)
        starting_phrase = result    
    print(len(result))
    
def draw():
    background(235, 235, 235)
    translate(width / 2, height * 0.95)
    # translate(0, height * 0.45)  # 3d in p5js starts centered
    rotateY(frameCount / 70.0)
    for symbol in result:
        if symbol == 'X':   # se symbol for igual a 'X'
            pass
        elif symbol in 'FS':   # else if 
                line(0, 0, 0, -step)
                translate(0, -step)
                rotateY(radians(-angle))
        elif symbol == '+':
            rotate(radians(-angle)) # + random(-5, 5)))
        elif symbol == '-':
            rotate(radians(+angle)) # + random(-5, 5)))
        elif symbol == '[':
            pushMatrix()
        elif symbol == ']':
            popMatrix()

def keyPressed():
    saveFrame("##.png") 
