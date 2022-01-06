# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
from random import choice

GRID_SIZE = 35

def setup():
    size(600, 600)
    strokeWeight(3)
    border = 50
    spacing = (width - border * 2) / GRID_SIZE
    Node.spacing = spacing
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            Node.nodes.append(Node(border + spacing / 2 + x * spacing,
                                   border + spacing / 2 + y * spacing))
    for node in Node.nodes:
        node.set_nbs()
    Node.nodes[0].current = True

def draw():

    background(245)
    for node in Node.nodes:
        node.plot_links()
        node.update()

class Node():
    nodes = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.current = False
        self.links = []
        self.cor = 0

    def plot_links(self):
        for node in self.links:
            stroke(0)
            line(node.x, node.y, self.x, self.y)

    def set_nbs(self):
        self.nbs, self.unvisited_nbs = [], []
        for node in Node.nodes:
            if node != self and dist(node.x, node.y,
                                     self.x, self.y) <= Node.spacing * 1.5:
                self.nbs.append(node)
                self.unvisited_nbs.append(node)

    def set_unvisited_nbs(self):
        self.unvisited_nbs = [node for node in self.nbs
                              if not node.visited]

    def update(self):
        self.set_unvisited_nbs()
        if self.current:
            self.visited = True
            if self.unvisited_nbs:
                rnd_choice = choice(self.unvisited_nbs)
                self.links.append(rnd_choice)
                self.current = False
                rnd_choice.current = True
                rnd_choice.visited = True
                rnd_choice.cor = self.cor + 1
            else:
                branch_nodes = [node for node in Node.nodes
                                if node.visited and node.unvisited_nbs]
                if branch_nodes:
                    rnd_choice = branch_nodes[-1] #choice(branch_nodes)
                    self.current = False
                    rnd_choice.current = True
                else:
                    noLoop()

def keyPressed():
    saveFrame("output.png")
