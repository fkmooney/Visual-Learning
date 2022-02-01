def setup():
    size(600,600, P3D) # 3d so no saveframe functionality

def draw():
    
    pict = createGraphics(600,600)
    pict.beginDraw()
    pict.fill(255,0,0)
    pict.strokeWeight(5)
    pict.square(0,0,600)
    pict.fill(245)
    pict.noStroke()
    pict.rect(38, 225-55+13, width-(2*38), 85+(2*5))
    pict.rect(33, 360-55+13, width-(2*30), 85+(2*5))
    
    font = createFont("Helvetica-Bold.ttf", 85)
    pict.textFont(font)
    pict.fill(30)
    pict.text("Plenty ought", 43, 255)
    pict.text("to be enough", 38, 390)
    pict.endDraw()
    
    # create each side with pict mapped on as texture
    beginShape()
    texture(pict)
    vertex(0, 0, -600, 0,0) # first three digits are vertex coords
    vertex(600, 0, -600, 600,0) # last two are pict coord to go at vertex
    vertex(600, 600, -600, 600,600)
    vertex(0,  600, -600, 0, 600)
    vertex(0, 0, -600, 0,0)
    endShape()
    
    beginShape()
    texture(pict)
    vertex(0, 600, -600, 0,0)
    vertex(600, 600, -600, 600,0)
    vertex(600, 600, 0, 600,600)
    vertex(0,  600, 0, 0, 600)
    vertex(0, 600, -600, 0,0)
    endShape()

    beginShape()
    texture(pict)
    vertex(0, 0, 0, 0,0)
    vertex(0, 0, -600, 600,0)
    vertex(0, 600, -600, 600,600)
    vertex(0,  600, 0, 0, 600)
    vertex(0, 0, 0, 0,0)
    endShape()    

    beginShape()
    texture(pict)
    vertex(600, 0, -600, 0, 0)
    vertex(600, 0, 0, 600, 0)
    vertex(600, 600, 0, 600,600)
    vertex(600,  600, -600, 0, 600)
    vertex(600, 0, -600, 0, 0)
    endShape()     

    beginShape()
    texture(pict)
    vertex(0, 0, 0, 0, 0)
    vertex(600, 0, 0, 600, 0)
    vertex(600, 0, -600, 600,600)
    vertex(0,  0, -600, 0, 600)
    vertex(0, 0, 0, 0, 0)
    endShape()    
    
    noLoop()
    
