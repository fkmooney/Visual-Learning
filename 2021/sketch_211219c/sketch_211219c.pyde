def setup():
  size(1440, 900)
  #strokeCap(ROUND)
  background(255, 255, 255)

  for k in range(30, 900, 30):
    ilist = list(range(20, 1440, 20)) 
    jlist = list(range(1440, 0, -20))
    
    for n in range(len(ilist)):
        l = ilist[n]
        m = jlist[n]

        if (l<700):
            strokeWeight(l/20)
            pushMatrix()  
            translate(l, k)
            rotate(radians((45 + random(l/5))))
            line(0, -10, 0, 10)
            popMatrix()   
        else:
            strokeWeight(m/20)
            pushMatrix();      
            translate(l, k);
            rotate(radians((45 + random(m/5))))
            line(0, -10, 0, 10)
            popMatrix()

def draw():
    b=1
  
def keyPressed():
    saveFrame("###.png")
