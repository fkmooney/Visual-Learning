increment = 0.01
detail = .99

def setup():
    size(600, 600)
    noLoop()
    
    # background 
    loadPixels()
    xoff = 0.0; # Start xoff at 0
    noiseDetail(8, detail)
  
    # For every x,y coordinate in a 2D space, calculate a noise and brightness value
    for x in range(0,width,1): 
        xoff += increment  # Increment xoff 
        yoff = 0.0  # For every xoff, start yoff at 0
        for y in range(0,height,1): 
            yoff += increment # Increment yoff
      
            # Calculate noise and scale by 255
            bright = noise(xoff, yoff) * 90 + 20
            if bright > 195:
                bright = 255 - 70

      
            # Set each pixel onscreen to a grayscale value
            pixels[x+y*width] = color(20,20,bright)

    updatePixels()
    

def draw():
    noFill()
    strokeWeight(50)
    stroke(245)
    rect(0,0,width,height)
    
def keyPressed():
    saveFrame("output.png")
