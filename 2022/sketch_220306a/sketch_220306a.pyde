# hans haacke blue sail

def setup():
    size(600, 600, P3D)
    background(245)
    frameRate(2)

def draw():
    t = millis()/500
    l = 2 #Spacing between points
    n = 150 #Number of points
    background(245)
    camera(width/2, height-100, 400, width/2, height/2, 0, 0, 1, 0)
    lights()

    points = []

    translate(width/2, height/2, 0)
    rotateX(float(mouseY)/height)
    rotateZ(TWO_PI-(((float(mouseX)/width)*TWO_PI+PI))+100)

    for i in range(n):
        for j in range(n):
            x2 = (l*i+l/2-l*n/2)
            y2 = (l*j+l/2-l*n/2)
            distance = dist(0, 0, x2, y2)
            z = exp(-distance/60)*sin(((distance)/20)-t*2)*40
            points.append(PVector(x2, y2, z))
        
    noFill()

    for i in range(n): 
        beginShape(QUAD_STRIP)
        for j in range(n-1):
            v = points[j+n*i]
            stroke(127+v.z*1.5, 127+v.z*1.5, 255)
            strokeWeight(1)
            vertex(v.x, v.y, v.z)
        endShape()
