# colormirror moons no. 11, 2020
# https://www.artnet.com/galleries/edition-galerie-hoffmann/regine-schumann

def setup():
    size(600, 600, P3D)  # 3d so no saveframe functionality
    noStroke()
    colorMode(HSB, 360,100,100)
    noLoop()

def draw():
    smooth()
    background(0)
    
    # wall light
    ambientLight(234, 70, 30,  300,300,-950) #HSB, Coord
    spotLight(234, 70, 20,  # HSB
              100, 300, 220, # xyz
              0, 0, -1,  # direction xyz, -1 y means pointed up
              1.7*PI, 3) # angle of cone and bias to middle"""
    spotLight(300, 70, 60,  # HSB
              360, 120, 220, # xyz
              0, 0, -1,  # direction xyz, -1 y means pointed up
              PI/2, 22) # angle of cone and bias to middle
    spotLight(300, 70, 60,  # HSB
              360, 490, 220, # xyz
              0, 0, -1,  # direction xyz, -1 y means pointed up
              PI/2, 22) # angle of cone and bias to middle

    # frame light
    ambientLight(300, 20, 20,  300,300,100) #HSB, Coord
    spotLight(300, 10, 100,  # HSB
              380, 300, 600, # xyz
              0, 0, -1,  # direction xyz, -1 y means pointed up
              0.4*PI, 12) # angle of cone and bias to middle
    
    #framed elements
    fill(316,60,100)
    rect(255,170,170,280)
    fill(40,0,80)
    arc(400, 310, 210, 210, PI*0.4, PI * 1.6, CHORD)
    fill(40,0,30)
    arc(265, 315, 110, 110, PI*1.4, PI * 2.6, CHORD)
    noFill()
    stroke(316,10,100)
    strokeWeight(3)
    rect(255,170,170,280)
    
    # wall
    noStroke()
    fill(40,0,100)
    cols = 40
    tam = width / cols *2
    for x in range(cols):
        for y in range(cols):
            fill(240,25,70)
            with pushMatrix():
                translate(x * tam-250,  y * tam-250, -400)
                box(30)

    
