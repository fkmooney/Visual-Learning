painting = False # dtermines if cursor drawing or not
colorchange = False

def keyPressed():
    if key=='d':
        saveFrame("output.png")

def mousePressed():
    if mouseButton == LEFT:
        fill(255,0,0)
        loop()
        
    if mouseButton == RIGHT:
        fill(30,145)
        loop()

def mouseReleased():
    noLoop()
    global painting
    painting = False

increment = 0.005
detail = 0.6

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
            bright = noise(xoff, yoff) * 100 + 170
      
            # Set each pixel onscreen to a grayscale value
            pixels[x+y*width] = color(50,50,bright)

    updatePixels()

def draw():

    global painting
    loosness = 10

    if not painting and frameCount > 1:
        line(mouseX,mouseY, mouseX,mouseY)
        painting = True
    elif painting:
        for x in range(0,10,1):
            for y in range(0,10,1):
                noStroke()
                circle(mouseX+x+random(-loosness,loosness),
                     mouseY+y+random(-loosness,loosness), 2)
