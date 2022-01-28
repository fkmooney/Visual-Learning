from itertools import islice, count

def setup():
    size(600, 600)
    background(245)
    stroke(30)
    strokeWeight(5)
    noFill() 

def draw():

    def seq(start,ends, step):
        assert (step != 0)
        sample_count = int(abs(ends - start) / step)
        return islice(count(start, step), sample_count) 
    
    def polygon(x, y, radius, npoints):
        angle = TWO_PI / npoints
        beginShape()
        for a in seq(0,TWO_PI, TWO_PI/6 ):
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            vertex(sx, sy)
        endShape(CLOSE)
            
    for i in range(0,130):    
        if (i%20 < 10):  
            if i%2 == 0:
                fill(255,0,0,60)         
                polygon(floor(i/10)*100 - 25*(floor(i/10)-1), (i%10)*50*sqrt(3)+25*sqrt(3), 50, 6)
            else:
                noFill()
                polygon(floor(i/10)*100 - 25*(floor(i/10)-1), (i%10)*50*sqrt(3)+25*sqrt(3), 50, 6)
            
        else:
            noFill() 
            polygon(floor(i/10)*100 - 25*(floor(i/10)-1), (i%10)*50*sqrt(3), 50, 6) 
            
    square(0,0,width)
    noLoop()
    
def keyPressed():
    saveFrame("output.png")
       
    
