# inspired by mel bochner's range 1979
def setup():
    size(600,600)
    background(245)
    translate(20,30)
    
    c = 0
    co = color(30,30,30)
    
    for x in range(47):
        if co == color(30,30,30):
            co = color(250,0,0)
        else:
            co = color(30,30,30)
        for y in range(47):
            fill(co)
            text('{:.0f}'.format(c), x*12, y*12)
            if c < 9:
                c = c+1
            else:
                c = 0
                if co == color(30,30,30):
                    co = color(250,0,0)
                else:
                    co = color(30,30,30)

    saveFrame("output.png")
            
            
