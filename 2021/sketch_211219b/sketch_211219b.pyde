GRID_SIZE = 20
distortion_amt = 30

def setup():
    global xo, yo
    size(600, 600)
    background(255,255,255)
    init_grid(GRID_SIZE)
    
def pairwise(iterable):
    import itertools
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b) 

def line_instersect(line_a, line_b):     
       
    x1, y1 = line_a.p1.x, line_a.p1.y
    x2, y2 = line_a.p2.x, line_a.p2.y
    x3, y3 = line_b.p1.x, line_b.p1.y
    x4, y4 = line_b.p2.x, line_b.p2.y
        
    try:
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
    except ZeroDivisionError:
        return
        
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
        
    x = line_a.p1.x + uA * (line_a.p2.x - line_a.p1.x)
    y = line_a.p1.y + uA * (line_a.p2.y - line_a.p1.y)
        
    return PVector(x, y)

def edges(poly_points):
        return pairwise(poly_points) + [(poly_points[-1], poly_points[0])] 
    
def inter_lines(L, poly_points):
        inter_points = []
        for p1, p2 in edges(poly_points):
            inter = line_instersect(Line(p1, p2), L)
            if inter:
                inter_points.append(inter)
        if  not inter_points:
            return []
        inter_lines = []
        if len(inter_points) > 1:
            inter_points.sort()
            pairs = zip(inter_points[::2], inter_points[1::2])
            for p1, p2 in pairs:
                if p2:
                    inter_lines.append(Line(PVector(p1.x, p1.y),
                                        PVector(p2.x, p2.y))) 
        return inter_lines

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def plot(self):
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


def draw():
    for c in Cell.cells:
        c.plot()

def init_grid(grid_size):
    Cell.border = 50
    Cell.spacing = (width - Cell.border * 2) / grid_size
    Cell.cells = []

    for x in range(0, grid_size, 2):
        for y in range(0, grid_size, 2):
                new_cell = Cell(x, y)
                Cell.cells.append(new_cell)
                Cell.grid[x, y] = new_cell

    Node.nodes = []
    for x in range(-1, grid_size+1, 2):
        for y in range(-1, grid_size+1, 2):
                new_node = Node(x, y)
                #Cell.cells.append(new_node)  # mudar!
                Cell.grid[x, y] = new_node   # extrarir do dict

    for c in Cell.cells:
        c.update_vers()
   
class Node():
    nodes = []
    grid = dict()

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing / 2 + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing / 2 + y * Cell.spacing 
        self.px += random(-1*distortion_amt, distortion_amt)
        self.py += random(-1*distortion_amt, distortion_amt)
        self.x = self.px
        self.y = self.py

class Cell():
    cells = []
    grid = dict()
    vers = []

    def __init__(self, x, y):
        self.ix = x
        self.iy = y
        self.px = Cell.border + Cell.spacing / 2 + x * Cell.spacing 
        self.py = Cell.border + Cell.spacing / 2 + y * Cell.spacing 
        self.vers = []        
      
    def plot(self):
        if len(self.vers) > 1:
            for n0, n1 in edges(self.vers):
                line(n0.px, n0.py, n1.px, n1.py)
        for l in self.lines:
            l.plot()

    def update_vers(self):
        v0 = Cell.grid.get((self.ix-1, self.iy-1))
        v1 = Cell.grid.get((self.ix-1, self.iy+1))
        v3 = Cell.grid.get((self.ix+1, self.iy-1))
        v2 = Cell.grid.get((self.ix+1, self.iy+1))
        self.vers = [v for v in [v0, v1, v2, v3] if v]
        self.lines = []
            
def keyPressed():
    saveFrame("###.png")
