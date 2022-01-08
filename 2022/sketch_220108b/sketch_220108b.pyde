def setup():
    size(600, 600)
    background(245)
    strokeWeight(1)
    stroke(30)
    noFill() 

def draw():
    translate(-20,0)
    
    inc = TWO_PI/133 # period
    amp = 20
    x_coord_adj = 20
    y_coord_adj = height*2/3+20
      
    # horizontal A
    pushMatrix()
    a = 9.5 # start point on y axis
    beginShape()
    for i in range(100, 500): # range moving across  
        curveVertex(x_coord_adj + i, y_coord_adj + sin(a) * amp)         
        a = a + inc
    endShape()
    popMatrix()

    # horizontal B
    pushMatrix()
    a = 9.5 # start point on y axis
    beginShape()
    for i in range(100, 500): # range moving across    
        curveVertex(x_coord_adj + i, y_coord_adj + sin(-a) * amp)       
        a = a + inc
    endShape()
    popMatrix()
            
    # vertical L A             
    pushMatrix()
    a =11.0 # start point on y axis
    x_coord_adj = 90
    y_coord_adj = -10
    beginShape()
    for i in range(100, 400): # range moving across    
        curveVertex(x_coord_adj + sin(a) * amp,i + y_coord_adj)       
        a = a + inc
    endShape()

    # vertical L B
    a =11.0 # start point on y axis
    beginShape()
    for i in range(100, 400): # range moving across    
        curveVertex(x_coord_adj + sin(-a) * amp,i + y_coord_adj)       
        a = a + inc
    endShape()
    popMatrix()
 
    # vertical R A
    a = 11.0 # start point on y axis
    x_coord_adj = 550
    pushMatrix()
    beginShape()
    for i in range(100, 400): # range moving across    
        curveVertex(x_coord_adj + sin(a) * -amp,i + y_coord_adj)       
        a = a + inc
    endShape()

    # vertical R B
    a = 11.0 # start point on y axis
    beginShape()
    for i in range(100, 400): # range moving across    
        curveVertex(x_coord_adj + sin(a) * amp,i + y_coord_adj)       
        a = a + inc
    endShape()
    popMatrix()
    
    # LEFT CORNER
    line(89,388,120,422)
    beginShape()
    curveVertex(89,388)
    curveVertex(89,388)
    curveVertex(75,405)
    curveVertex(74,423)
    curveVertex(87,435)
    curveVertex(105,432)
    curveVertex(120,418)
    curveVertex(124,414)
    endShape()
    
    # RIGHT CORNER
    line(515,422,551,388)
    beginShape()
    curveVertex(511,414)
    curveVertex(518,420)
    curveVertex(532,432)
    curveVertex(550,435)
    curveVertex(565,423)
    curveVertex(566,405)
    curveVertex(549,387)
    curveVertex(546,383)
    endShape()   
          
    noLoop()

def keyPressed():
    saveFrame("output.png")
