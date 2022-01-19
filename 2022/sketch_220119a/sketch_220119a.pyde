# pixelates into B&W squares w size of square used to shade
resolution = 6
darkness = 0.8

def setup():
    size(400, 500)
    background(255)
    global img
    img = loadImage("portait.jpg")
    img.resize(width, height);
    noStroke() 
    fill(0)
      
def draw():

    for x in range(0, width, resolution):  
        for y in range(0, height, resolution):
            xc, yc = resolution / 2 + x, resolution / 2 + y
            cor = img.get(xc, yc) # reads the color of the pixel at the designated coord
            dark = 255 - brightness(cor)  # 0 to 255
            temp = dark / 255.0 * resolution
            if temp > resolution * 0.37:
                square(xc, yc, temp * darkness)
    noLoop() 
    
def keyPressed():
    saveFrame("ouput.png")
    
