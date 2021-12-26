# triangle pairs on reg polygon vertices with no more than 1 point in common: 100

from itertools import product, combinations, permutations
from line_geometry import poly_edges, simple_intersect
import random

space, border = 75, 75 # sapce for each shape, increase in relation to size of canvas

def setup():
    global tri_combos, W, H, position, num
    size(900, 900) # size of canvas
    strokeJoin(ROUND)
    points = hex_points(0, 0, 1) # last digits is size of triangles in slot
    # all triple point combinations on a grid
    point_combinations = (list(combinations(points, 3)))
       # filter out colinear triples
    triangles = [pts for pts in point_combinations
                 if area(pts) != 0 # removes 3 colinear points
                 ]
    all_2tri_combos = list(combinations(triangles, 2))
    # all_2tri_combos = random.sample(all_2tri_combos,2)
    tri_combos = [(ta, tb,) for ta, tb, in all_2tri_combos
                  if  len(set(ta) | set(tb)) > 3 
                  # and not triangle_intersection(ta, tb) # finds all w no intersection
                  ]
    # tri_combos = [(ta, tb) for i, (ta, tb) in enumerate(tri_combos[:19])  # for debug!
    #               if not same_angles(ta, tb, i)]
    #tri_combos.sort(key=lambda c: c[1]) # digit indicates which trangle to sort by
    #tri_combos.sort(key=lambda c: area(c[0]) - area(c[1])) # orig sort option
    random.shuffle(tri_combos) # randomizes order
    println("Number of triangle combinations: {}".format(len(tri_combos)))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    # tri_combos = [()] + tri_combos # to add a space in the 1st grid position
    background(255)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(tri_combos):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                draw_combo(i)
                popMatrix()
                i += 1

    saveFrame('combos.png')

def hex_points(x, y, sizea):
    # the last digit in the two lines below determines number of points
    # hexagon = 60 because 360/60 = 6
    # 10 sided = 36 because 360/36 = 10
    return [(x + sizea * cos(PI / 180 * 45 * i),
             y + sizea * sin(PI / 180 * 45 * i))
             for i in range(8)] # controls the number of points tris can use
    

def area(p):
   return abs(p[1][0] * (p[2][1] - p[0][1]) +
              p[2][0] * (p[0][1] - p[1][1]) +
              p[0][0] * (p[1][1] - p[2][1]))

def triangle_intersection(ta, tb, i=None):
    for ea in poly_edges(ta):
        for eb in poly_edges(tb):
            if simple_intersect(shrink(ea), shrink(eb)):
            # if abs(edge_angle(ea) - edge_angle(eb)) < 0.1:
                return True
    return False

def shrink(seg):
    (xa, ya), (xb, yb) = seg
    new_a = lerp(xa, xb, 0.1), lerp(ya, yb, 0.1)
    new_b = lerp(xa, xb, 0.9), lerp(ya, yb, 0.9)
    return (new_a, new_b)

def edge_angle(edge):
        pa, pb = edge
        ea = atan2(pa[1] - pb[1], pa[0] - pb[0])
        return ea + PI if ea < 0 else ea % PI
    
def draw_combo(n):
    noStroke()
    siz = space / 3.5 # size of shapes in its allocated space
    colors = (color(200, 200, 0), color(0, 200, 200, 128))
    for tri, c in zip(tri_combos[n], colors):
        fill(c)
        (x0, y0), (x1, y1), (x2, y2) = tri[0], tri[1], tri[2]
        triangle(x0 * siz, y0 * siz,
                 x1 * siz, y1 * siz,
                 x2 * siz, y2 * siz)
