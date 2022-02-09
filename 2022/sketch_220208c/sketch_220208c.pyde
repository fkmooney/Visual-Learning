from random import choice

class StableWalker(object):

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.start_x = None
        self.start_y = None

    def move(self):
        self.start_x = self.posx
        self.start_y = self.posy

        x = self.posx + random(-70,70)
        y = self.posy + random(-10,50)

        # keeps away from sides of canvas
        if x > width * 0.95:
            x = width * random(0.8,0.9)   
        elif x < width * 0.05:
            x = width * random(0.1,0.2)

        self.next_pos = PVector(x, y)
        self.posx = self.next_pos.x
        self.posy = self.next_pos.y

    def display(self):
        if self.start_y > self.next_pos.y:
            if self.next_pos.y < 1:
                self.next_pos.y = 5
            elif self.next_pos.y < 100:
                self.next_pos.y = self.next_pos.y + random(20,100)
            else:    
                self.next_pos.y = self.next_pos.y * 1.5 # reduce amt going upward    
        print(self.next_pos.y)
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
    stroke(30)
    repli_walker(0.1,steps)

    repli_walker(0.2,steps)

    repli_walker(0.3,steps)

    repli_walker(0.4,steps)

    repli_walker(0.5,steps)

    repli_walker(0.6,steps)

    repli_walker(0.7,steps)

    repli_walker(0.8,steps) 
    repli_walker(0.9,steps) 
    repli_walker(0.75,steps) 
    repli_walker(0.5,steps) 
    repli_walker(0.25,steps)    
    noLoop()
        
def keyPressed():
    saveFrame("output.png")
