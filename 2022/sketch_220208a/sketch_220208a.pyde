# Inspired by Brice Marden

def setup():
    size(600, 600)
    background(245)
    GRID_SIZE = 20
    border = 20
    spacing = (width - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            Ponto.PONTOS.append(Ponto(border + spacing / 2 + i * spacing,
                                      border + spacing / 2 + j * spacing)
                                )
    for p in Ponto.PONTOS:
        p.set_neighbours()
            
def draw():
    #background(0)
    for p in Ponto.PONTOS:
        p.update()

    if frameCount > 800 and not frameCount % 2:
        noLoop()

def keyPressed():
    saveFrame("ouput.png")
        
class Ponto():
    PONTOS = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = x
        self.py = y
        
    def set_neighbours(self):
        self.ort_ngb = [] # orthogonal neighbours
        self.dia_ngb = [] # diagonal neighbours
        for p in Ponto.PONTOS:
            d = dist(p.px, p.py, self.px, self.py)
            if  Ponto.spacing * 1.41 < d < Ponto.spacing * 1.42:
                self.dia_ngb.append(p)
            elif  d < Ponto.spacing * 1.41:
                self.ort_ngb.append(p)

    def update(self):
        rx = random(-0.5, 0.5)
        ry = random(-0.5, 0.5)
        if abs(self.px + rx - self.x) < Ponto.spacing * 0.25:
            self.px += rx
        if abs(self.py + ry - self.y) < Ponto.spacing * 0.25:
            self.py += ry
        self.plot()

    def plot(self):
        for p in self.ort_ngb + self.dia_ngb:
            d = dist(p.px, p.py, self.px, self.py)
            if  d < Ponto.spacing * 0.9:
                stroke(30)    
                line(p.px, p.py, self.px, self.py)
                
