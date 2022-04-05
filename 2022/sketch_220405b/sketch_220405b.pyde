H = 30
W = 60

def setup():
    size(600, 600)
    noStroke()    
    background(245,100,100)
    fill(100,30,210)
    cols = width / W
    rows = height / H
    for row in range(rows):
        for col in range(cols):
            x0, y0 = col * W, row * H
            n = 0.5 + (0.25 * sin(degrees(col) / (1 + 300)) +
                       0.25 * sin(degrees(row) / (1 + 100)))
            third_x = x0 + W * n
            triangle(x0, y0, x0 + W, y0, third_x, y0 + H)
            
    saveFrame("output.png")
            
