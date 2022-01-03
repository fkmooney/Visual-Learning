def quarter(tam, adj):
    translate(-tam/2,-tam/2)
    for x in range(0, width/2, tam):
        for y in range(0, height/2, tam):
            with pushMatrix():
                translate(x + tam/2, y + tam/2)
                noFill()
                                
                #back
                beginShape()
                vertex(0, 0, 0)
                vertex(tam, 0, 0)
                vertex(tam, tam, 0)
                vertex(0, tam, 0)
                vertex(0, 0, 0)
                endShape()
                
                #front
                noFill() 
                beginShape()
                vertex(tam, 0, 0)
                vertex(tam, 0, tam)
                vertex(tam, tam, tam)
                vertex(tam, tam, 0)
                vertex(tam, 0, 0)
                endShape()
                            
                #side
                fill(0)
                beginShape()
                vertex(0, 0, 0)
                vertex(0, 0, tam)
                vertex(0, tam, tam)
                vertex(0, tam, 0)
                vertex(0, 0, 0)
                endShape() 
                        
                #top
                fill(150,0,250)
                beginShape()
                vertex(0, tam, 0)
                vertex(0, tam, tam*2)
                vertex(tam, tam, tam*2)
                vertex(tam, tam, 0)
                vertex(0, tam, 0)
                endShape() 
                
                #top half
                fill(0,0,0)
                beginShape()
                vertex(tam/2, tam, 0)
                vertex(tam/2, tam, tam*2)
                vertex(tam, tam, tam*2)
                vertex(tam, tam, 0)
                vertex(tam/2, tam, 0)
                endShape() 
                
                #top half o clean up drip-throughs
                fill(0,0,0)
                beginShape()
                vertex(tam/2, tam+adj, 0)
                vertex(tam/2, tam+adj, tam*2)
                vertex(tam, tam+adj, tam*2)
                vertex(tam, tam+adj, 0)
                vertex(tam/2, tam+adj, 0)
                endShape() 




def setup():
    size(600, 600,P3D)
    fill(255)
    #rectMode(CENTER)

def draw():
    background(0,0,0)
    tam = 60
    quarter(tam,1)
    rotate(radians(90))
    translate(width/2+tam/2,-height/2-tam/2)
    quarter(tam,-1)
    translate(width/2+tam/2,-height/2+tam/2)
    rotate(radians(90))
    quarter(tam,1)
    translate(width/2+tam/2,height/2+tam/2)
    rotate(radians(90))
    quarter(tam,-1)
                                                                                                                                                          
    noLoop()

def keyPressed():
    saveFrame("output.png")
