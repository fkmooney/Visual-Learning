"""
sketch_2022_07_07 - d'aprés Antonio Maluf 1926—2005
"""
def setup():
    size(800, 800)
    background(220)    
    rectMode(CENTER)
    noStroke()
    step = 40
    hs = int(step / 2)
    speed = 1 / 20
    xoff = 100
    t = frameCount
    for y in range(hs, height-10, step): 
        for x in range(hs, width-10, step):
            xoff = xoff + .1
            w = hs + hs * noise(x * speed + xoff, t * speed) * 0.75
            h = hs + hs * noise(y * speed, t * speed) * 0.75
            fill(0)
            rect(x, y, w, h)
            next_x, next_y = x + step, y + step
            next_w = hs + hs * noise(next_x * speed + xoff, t * speed) * 0.75
            next_h = hs + hs * noise(next_y * speed, t * speed) * 0.75
            fill(255, 100, 0)
            xb = (x + w / 2 + next_x - next_w / 2) / 2
            yb = (y + h / 2 + next_y - next_h / 2) / 2
            wb = step - w /2 - next_w / 2
            hb = step - h /2 - next_h / 2
            rect(xb, yb, wb, hb)
            
    saveFrame("output.png")
