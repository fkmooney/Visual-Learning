S=600
def setup():
 size(S,S)
 colorMode(HSB)
 background(0)
 x=0
 f=0

 while x<S:
  y=0
  while y<S+8:
   h = 18 * noise(x * .01, (y+f) * .01, f * .01)
   fill(h*10,155,255)
   circle(x,y,min(8,h))
   y+=h
  x+=8 
  
  saveFrame("output.png")
  
