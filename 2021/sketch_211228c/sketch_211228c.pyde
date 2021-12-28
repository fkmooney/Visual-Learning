from random import choice

class GridElement(object):
    def __init__(self, x, y, i, j, w, h, grid):
        self.x, self.y = x, y
        self.i, self.j = i, j
        self.width, self.height = w, h
        self.grid = grid

class BaseGrid(object):

    def __init__(self, x, y, num_rows, grid_elem_size):
        self.grid_x = x
        self.grid_y = y
        self.num_rows = num_rows
        self.grid_elem_size = grid_elem_size

    def get_grid_positions(self):
        grid_width_limit = self.grid_x + self.num_rows * self.grid_elem_size
        grid_height_limit = self.grid_y + self.num_rows * self.grid_elem_size

        x_positions = []
        acc = self.grid_x
        while acc < grid_width_limit:
            x_positions.append(acc)
            acc += self.grid_elem_size

        y_positions = []
        acc = self.grid_y
        while acc < grid_width_limit:
            y_positions.append(acc)
            acc += self.grid_elem_size

        for i, x in enumerate(x_positions):
            for j, y in enumerate(y_positions):
                yield GridElement(x, y, i, j, self.grid_elem_size, self.grid_elem_size, self)

class VirtualGrid(BaseGrid):

    def draw(self, func, *f_args, **f_kwargs):
        for grid_elem in self.get_grid_positions():
            with pushMatrix():
                translate(grid_elem.x, grid_elem.y)
                self.draw_elem(grid_elem, func, *f_args, **f_kwargs)

    def draw_elem(self, grid_elem, func, *f_args, **f_kwargs):
        func(*f_args, **f_kwargs)

class Grid(VirtualGrid):

    def draw_elem(self, grid_elem, func, *f_args, **f_kwargs):
        func(grid_elem.i, grid_elem.j, self.grid_elem_size)

WHITE = color(245, 245, 245)
BLUE = color(0, 0, 255)
colors = []
elem_size = 90.0
s = elem_size / 2
diff = 1

def pattern(i, j, size):
    global s
    half = size / 2
    offset = 5
    ellipse(half, half, s, s)

elem_size = 90.0
num_rows = 900 / elem_size

def setup():
    size(900, 900)
    stroke(BLUE)
    strokeWeight(6)
    noFill()

    for i in range(int(num_rows)):
        colors.append(choice([BLUE]))

def draw():
    global s, diff
    background(WHITE)
    grid = Grid(0, 0, num_rows, elem_size)
    grid.draw(pattern)

    s += diff
    if s > 4 * elem_size or s < elem_size / 2:
        diff *= -1

def keyPressed():
    saveFrame("#####.png") 
