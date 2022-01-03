def quarter(tam, ln):
    
    for x in range(0, width/2, tam):
        for y in range(0, height/2, tam):
            with pushMatrix():
                translate(x , y )
                noFill()
                """
                #front
                stroke(255)
                beginShape()
                vertex(0, 0, 0)
                vertex(tam,0,0)
                vertex(tam, tam, 0)
                vertex(0, tam, 0)
                vertex(0, 0, 0)
                endShape() 
                """
                #bottom side
                fill(250,250,0)
                beginShape()
                vertex(0, tam, 0)
                vertex(tam,tam,0)
                vertex(tam, tam, -ln*tam)
                vertex(0, tam, -ln*tam)
                vertex(0, tam, 0)
                endShape()
                
                #bottom half
                fill(0)
                beginShape()
                vertex(0, tam, 0)
                vertex(tam/2,tam,0)
                vertex(tam/2, tam, -ln*tam)
                vertex(0, tam, -ln*tam)
                vertex(0, tam, 0)
                endShape()
                
                # get rid of drip throughs
                fill(0)
                beginShape()
                vertex(0, tam-1, 0)
                vertex(tam/2,tam-1,0)
                vertex(tam/2, tam-1, -ln*tam)
                vertex(0, tam-1, -ln*tam)
                vertex(0, tam-1, 0)
                endShape()
                
                 
                #right side
                fill(0)
                beginShape()
                vertex(tam, 0, 0)
                vertex(tam,tam,0)
                vertex(tam, tam, -ln*tam)
                vertex(tam, 0, -ln*tam)
                vertex(tam, 0, 0)
                endShape()                    
            

def setup():
    size(600, 600,P3D)
    fill(255)
    #rectMode(CENTER)

def draw():
    background(0,0,0)
    tam = 50
    depth = 6
    translate(width/2,height/2)

    quarter(tam,depth)
    rotate(radians(90))
    quarter(tam,depth)
    rotate(radians(90))
    quarter(tam,depth)
    rotate(radians(90))
    quarter(tam,depth)
                                                                                                                                                          
    noLoop()

def keyPressed():
    saveFrame("output.png")
