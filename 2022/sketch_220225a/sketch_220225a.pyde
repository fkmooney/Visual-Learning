def setup():
    background(245)
    size(600,600)
    
def draw():
    noStroke()
    translate(width/2, height/2)
    
    dim = 130
    
    fill(70,100,200)
    for i in range(0,6):
        rotate( TWO_PI/6 )
        circle( 150, 0, dim )
    
    fill(200,100,100)
    for i in range(0,6):
        rotate( TWO_PI/6 )    
        arc(150, 0, dim, dim, PI * 0.67,PI *1.33 )
    
    fill(100,70,200)
    circle(0,0,dim)
    
    fill(30)
    textSize(7)
    text("""
def setup():
    background(245)
    size(600,600)
    
def draw():
    noStroke()
    translate(width/2, height/2)
    
    dim = 140
    
    fill(70,100,200)
    for i in range(0,6):
        rotate( TWO_PI/6 )
        circle( 150, 0, dim )
    
    fill(200,100,100)
    for i in range(0,6):
        rotate( TWO_PI/6 )    
        arc(150, 0, dim, dim, PI * 0.67,PI *1.33 )
    
    fill(100,70,200)
    circle(0,0,dim)         

""",-width/2+10, -height/2+330)
    
    
    
    saveFrame("output.png")
