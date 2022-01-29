def setup():
    size(600, 600)
    background(245)
    strokeWeight(10)
    stroke(30)
    noFill()

def draw():
    # square 1
    for x in range(0,width/2,20):
        clip(0,0,width/2, height/2)
        line(x,0,x,height)
        
    # square 2
    for y in range(0,height/2,20):
        clip(width/2, 0,width,height/2)
        line(width/2,y,width,y)
   
     # sqaure 3
    for x in range(0,width,25):
        clip(0,height/2,width/2, height)       
        line(x-width/2,height/2,x,height)
        
    # sqaure 4
    for x in range(0,width,25):
        clip(width/2, height/2, width, height)       
        line(x+width/2,height/2,x,height)
    
    noClip()
    
    # framing           
    line(width/2,0, width/2,height)
    line(0,height/2, width,height/2)
    strokeWeight(20) 
    square(0,0, height)
             
    noLoop()    

def keyPressed():
    saveFrame("output.png")
