S=600
def setup():
 size(S,S)
 colorMode(HSB)
 background(0)
 x=0
 f=0

 while x<S:
  y=0
  h = 18 * noise(x * .01, (y+f) * .01, f * .01)
  while y<S+8:
   
   fill(h*10,155,255)
   rect(x,y,h,h)
   y+=h
  x+=h 
  
  saveFrame("output.png")
  
