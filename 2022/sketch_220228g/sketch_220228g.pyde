def setup():
  size(600, 600, P3D)
  background(245)

def draw():
  strokeWeight(0.3)
  stroke(30)
  noFill()
  def orb(wid, x, y):
    pushMatrix()
    translate(x, y) # start from the core
    z = random(wid/2-50)       # get a random radius
    rotateX(random(TWO_PI))      # rotate on X axis randomly
    rotateY(random(TWO_PI))      # rotate on Y axis randomly
    t = sqrt(sq(wid/2-50)-sq(z))# calc distance from core to center of circle
    translate(0, 0, t)          # go to center of circle
    ellipse(0, 0, 2*z, 2*z)     # draw a circle on the surface
    popMatrix()
      
  if frameCount  < 180:
    orb(600,300,300)

  if 200 < frameCount  < 330:
    orb(200,200,200)
    orb(200,320,210)
    orb(200,210,320)
    orb(200,330,330)
    
  if frameCount  > 330:    
    saveFrame("output.ong")
    noLoop()
