# On Kawara, 24,698 Days (100 Years Calendar), 2000.

def setup():
    size(600,600)
    background(245)
    stroke(30)
    strokeWeight(0)
    translate(0,-6)
    
    border = 5
    fill(255,255,0)
    for x in range(border, 365+ border):
        for y in range(45):
            circle(x*1.6,50+y*12,2)
            
    for x in range(border,border + 180):
        fill(245)
        circle(x*1.6, 50,2)
    
    for x in range(border+60,365+ border):
        fill(245)
        circle(x*1.6, 50+44*12 ,2)  
    
    fill(30)
    text("JAN      FEB       MAR       APR      MAY       JUN       JUL       AUG       SEP       OCT       NOV       DEC",25,42)
    saveFrame("output.png")
    
