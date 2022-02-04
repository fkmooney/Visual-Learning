def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB, 360,100,100)

def draw():
    smooth()
    background(0)
    rotateY(radians(20))
    translate(-30,0,0)

    # front light
    spotLight(61, 70, 360,  # HSB
              300, 200, -250, # xyz
              0, 0, -1,  # direction xyz, -1 y menas pointed up
              1.5*PI, .3) # angle of cone and bias to middle
    
    stroke(245)
    strokeWeight(5)
    strokeCap(ROUND)
    line(300,200,-593, 300,600,-400)
    
    noStroke()
    
    # front hall
    fill(40,0,360)
    beginShape()
    vertex(0, 600, -600, 0,0)
    vertex(600, 600, -600, 600,0)
    vertex(600, 600, 0, 600,600)
    vertex(0,  600, 0, 0, 600)
    vertex(0, 600, -600, 0,0)
    endShape()

    beginShape()
    vertex(0, 0, 0, 0,0)
    vertex(300, 0, -600, 600,0)
    vertex(300, 600, -600, 600,600)
    vertex(0,  600, 0, 0, 600)
    vertex(0, 0, 0, 0,0)
    endShape()    

    beginShape()
    vertex(300, 0, -600, 0, 0)
    vertex(600, 0, 0, 600, 0)
    vertex(600, 600, 0, 600,600)
    vertex(300,  600, -600, 0, 600)
    vertex(300, 0, -600, 0, 0)
    endShape()     

    beginShape()
    vertex(0, 0, 0, 0, 0)
    vertex(600, 0, 0, 600, 0)
    vertex(600, 0, -600, 600,600)
    vertex(0,  0, -600, 0, 600)
    vertex(0, 0, 0, 0, 0)
    endShape()
    
    noLoop()
