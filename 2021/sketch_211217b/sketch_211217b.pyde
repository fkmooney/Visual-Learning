def setup():
    global sqSide, sqRows, sqCols, xoffset, yoffset;
    size(800, 600, P2D);  ### CHANGE 1
    sqSide = 80;          ### CHANGE 2
    sqRows = 5;          ### CHANGE 3  
    sqCols = 7;          ### CHANGE 4
    xoffset = (width -  sqCols * sqSide) / 2.0;
    yoffset = (height - sqRows * sqSide) / 2.0;
    
def draw():
    if frameCount < 5:
        # For a white background. 
        background(255, 255, 255);            ### CHANGE 5
        albers(100, 160, 150, 5, 100, 200, 20); ### CHANGE 6
        
        # Saves your image as a .png file.
        saveFrame("frames//####.png")
    
def albers(R, G, B, delta_R, delta_G, delta_B, numseed):
    import random 
    global sqSide, sqRows, sqCols;
    
    # Sets the seed of the random number generator.
    random.seed(numseed);
    
    for x in range(sqCols):
        for y in range(sqRows):
            # We don't want the inidividual rectangles outlined.
            strokeWeight(0);
            
            # So brighter rectangles are not always on the right.
            if random.random() < 0.5:
                sign = 1
            else:
                sign = -1;
             
            # Generating randomness in the colors.       
            delta_R2 = sign * random.randrange(delta_R);
            delta_G2 = sign * random.randrange(delta_G);
            delta_B2 = sign * random.randrange(delta_B);
       
                
            # Draws the left background rectangle.
            fill(R - delta_R2, G - delta_G2, B - delta_B2);
            myshape([[0, 0], [0, 1], [0.5, 1], [0.5,0]], x, y);
   
            # Draws the right background rectangle.
            fill(R + delta_R2, G + delta_G2, B + delta_B2);
            myshape([[0.5, 0], [0.5, 1], [1, 1], [1, 0]], x, y);
    
            # Draws the two central rectangles the same color.
            fill(R, G, B);
            myshape([[0.15, 0.15], [0.15, 0.85], [0.35, 0.85], [0.35, 0.15]], x, y);
            myshape([[0.65, 0.15], [0.65, 0.85], [0.85, 0.85], [0.85, 0.15]], x, y);
       
       
def myshape(vertices, x, y):    
    s = createShape();
    s.beginShape();
    [s.vertex((v[0] + x) * sqSide + xoffset, 
              height - ((v[1] + y) * sqSide + yoffset)) for v in vertices];
    s.endShape(CLOSE);
    shape(s, 0, 0);
    
