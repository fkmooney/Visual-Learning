from random import choice

STROKE = color(245,220,0)
WHITE_WITH_ALPHA = color(245, 245, 245, 20)

ANGLES = [90, 180, 270, 360]
DISTANCES = [10 * (i + 1) for i in range(0,20,2)]

class StableWalker(object):

    def __init__(self, pos):
        self.pos = pos
        self.start_pos = None
        self.end_pos = None
        self.walking_distance = 0
        self.angle = None

    def move(self):
        self.start_pos = self.pos

        self.angle = radians(choice([a for a in ANGLES if not radians(a) == self.angle]))
        self.walking_distance = choice(DISTANCES)
        
        if 3 < self.angle < 4 or 6 < self.angle < 7: # makes hor lines longer than vert
            self.walking_distance = self.walking_distance * 0.2
        
        x = self.pos.x + cos(self.angle) * self.walking_distance
        y = self.pos.y + sin(self.angle) * self.walking_distance

        if x > width * 0.9:
            x = width * random(0.8,0.9)   
        elif x < width * 0.1:
            x = width * random(0.1,0.2) 
        if y > height * 0.7:
            y = height * random(0.6,0.7)
        elif y < height * 0.3:
            y = height * random(0.3,0.4)

        self.next_pos = PVector(x, y)
        self.pos = self.next_pos

    def display(self):
        stroke(STROKE)
        line(self.start_pos.x, self.start_pos.y, self.next_pos.x, self.next_pos.y)

def setup():
    global walker1, walker2
    size(600, 600)
    background(WHITE_WITH_ALPHA)
    strokeWeight(2)
    stroke(STROKE)
    frameRate(24)
    start1 = PVector(width/4, height/4)
    walker1 = StableWalker(start1)
    
    start2 = PVector(width*3/4, height*3/4)
    walker2 = StableWalker(start2)

def draw():
    global walker1, walker2

    walker1.move()
    walker1.display()
    
    walker2.move()
    walker2.display()

    if  frameCount > 300:
        noLoop()
        
def keyPressed():
    saveFrame("output.png")
