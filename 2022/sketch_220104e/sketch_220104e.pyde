def setup():
    size(600,600)  
    background(0)

    noFill()
    
def draw():

    tam = 60
    strokeWeight(tam/4)
    stroke(255,230)
    translate(width/2,height/2)
    for x in range(0, width, tam):  
        radius = width-x-tam/4
        circle(0,0,radius)

    stroke(250,0,160,180)
    translate((width/9)*2, 0) # move across horizontally
    for x in range(0, width, tam):  
        radius = width-x-tam/4
        circle(0,0,radius)




    noLoop()
    
def keyPressed():
    saveFrame("output.png")    

    
