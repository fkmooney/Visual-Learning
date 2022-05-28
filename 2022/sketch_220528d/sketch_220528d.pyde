S=600
def setup():
 size(S,S)
 colorMode(RGB)
 background(0)
 x=0
 f=0
 w=8
 border = 0

 while x<S:
  y=0
  w = max(18 * noise(x * .01, (y+f) * .01, f * .01),4)
  while y<S+8:
   h = max(20 * noise(x * .01, (y+f) * .01, f * .01),4)
   fill(h*15,155,150)
   rect(x,y,w,h)
   y+=h+border
  x+=w+border
 
  
  saveFrame("output.png")
  
