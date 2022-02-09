from random import choice

class StableWalker(object):

    def __init__(self, posx, posy):
        self.initx = posx
        self.posx = posx
        self.posy = posy
        self.start_x = None
        self.start_y = None

    def move(self):
        self.start_x = self.posx
        self.start_y = self.posy

        x = self.initx + random(-50,50)
        y = self.posy + random(-5,50)

        # keeps away from sides of canvas
        if x > width * 0.95:
            x = width * random(0.9,0.95)   
        elif x < width * 0.05:
            x = width * random(0.05,0.1)

        self.next_pos = PVector(x, y)
        self.posx = self.next_pos.x
        self.posy = self.next_pos.y

    def display(self):
        if self.start_y > self.next_pos.y:
            if self.next_pos.y < 1:
                self.next_pos.y = 5
            elif self.next_pos.y < 100:
                self.next_pos.y = self.next_pos.y + random(20,100)
            elif self.next_pos.y > self.start_y:
                self.next_pos.y = self.next_pos.y * 3                                
            else:    
                self.next_pos.y = self.next_pos.y * 1 # reduce amt going upward    
        curveVertex(self.next_pos.x, self.next_pos.y)

def repli_walker(start, step):
    noFill()
    beginShape()
    walker1 = StableWalker(width*start, -10)
    curveVertex(width*start, -5)
    curveVertex(width*start, -5)
    
    for c in range(step):
        walker1.move()
        walker1.display()
    endShape()

def setup():
    size(600, 600)
    background(245)
    strokeWeight(8)
    
def draw():
    steps = 50
    coloru = 120
    stroke(random(20,coloru))
    repli_walker(0.1,steps)
    stroke(random(20,coloru))
    repli_walker(0.2,steps)
    stroke(random(20,coloru))
    repli_walker(0.3,steps)
    stroke(random(20,coloru))
    repli_walker(0.4,steps)
    stroke(random(20, coloru))
    repli_walker(0.5,steps)
    stroke(random(20,coloru))
    repli_walker(0.6,steps)
    stroke(random(20, coloru))
    repli_walker(0.7,steps)
    stroke(random(20,coloru))
    repli_walker(0.8,steps) 
    stroke(random(20,coloru))
    repli_walker(0.9,steps) 

    noLoop()
        
def keyPressed():
    saveFrame("output.png")
