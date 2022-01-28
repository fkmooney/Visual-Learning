def setup():
  size(585, 600)
  background(245)
  stroke(30)
  strokeWeight(5)

def draw():
  translate(0,20)
  edge = 117
  posx = edge/2
  posy = edge/4
  row = 7

  for i in range(0, row):
    if (i%2==0):
      posx = edge/2
      col = 8    
    else:
      posx = -edge
      col = 10
    
    for j in range(0,col):
      fill(255,0,0,50)
      triangle(posx-edge/2, posy+edge*0.85/2, 
           posx+edge/2, posy+edge*0.85/2, 
           posx, posy-edge*0.85/2)
      posx += edge
    
    posy += edge * 1.73/2
    
  noLoop() 
    
def keyPressed():
    saveFrame("ouput.png")
