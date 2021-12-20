import math
import sys
from random import shuffle, seed

################################################################################
# Global variables
################################################################################

rand_seed = 1171989
#seed(rand_seed)  # comment out to get diff version each time
anchors = []
len_anchors = 0
count = 0 # Counter to allow for tracking draw() runs

################################################################################
# Knobs to turn
################################################################################

dimension = 600  # width and height of canvas
step = 1 # does little
num_anchors = 9 # affects shape
radius = dimension/(.001*step) # Radius of individual circle

colorhue = 86 # 0-100 valune
colorsat = 20 # 0-100 value good as is
colorbal = 96 # 0-100 value
coloralpha = 4 # 0-100 value good as is

################################################################################
# setup() 
# function gets run once at start of program
################################################################################

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(dimension, dimension) # (width, height)
    
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity(2))  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
    background(0, 0, 100)
        
    # Determine anchor points around circle for the curves to hit
    global anchors, len_anchors
    anchors = range_float(0+PI/2, TWO_PI+PI/2, TWO_PI/num_anchors)
    len_anchors = len(anchors)

    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit) 

################################################################################
# draw() 
################################################################################

def draw():
    # Loop counter to control number of draw() runs
    global count
    if count >= len_anchors-1:
        sys.exit(0)
    count += 1

    # Moves origin to center of image so (0,0) becomes center instead of (w/2,h/2)
    #trans_moda = 2 # this centers image x
    #trans_modb = 2 # this centers image y
    trans_moda = random(0,2)
    trans_modb = random(0,2)
    translate(dimension/trans_moda, dimension/trans_modb)
        
    ##############################################################################
    # Actual shape drawing begins
    ##############################################################################
    w_step = dimension/step
    h_step = dimension/step
              
    noStroke()
    ##############################################################################
    fill(colorhue, colorsat, colorbal, coloralpha) # changes color  ##############
    ##############################################################################
    for j in range(10):
        x = random(0, dimension)
        y = random(0, dimension)
        for i in range(10):
            beginShape()
            draw_yarn_ball(x, y, dimension/2*0.7)
            endShape()
    
################################################################################
# Functions
################################################################################

def draw_yarn_ball(x_center, y_center, radius):
    # Get three start/end points. The curve needs to retrace these 3 points to connect in a smooth loop 
    # https://forum.processing.org/two/discussion/14849/how-to-form-a-smooth-loop-using-curve
    x_0, y_0 = circle_points(x_center, y_center, radius, random_list_value(anchors))
    curveVertex(x_0, y_0)
    x_1, y_1 = circle_points(x_center, y_center, radius, random_list_value(anchors))
    curveVertex(x_1, y_1)
    x_2, y_2 = circle_points(x_center, y_center, radius, random_list_value(anchors))
    curveVertex(x_2, y_2)

    # Shuffle the list to allow for randomized points around the circle
    shuffle(anchors)
    
    # Loop through list of anchor points and draw curves between them (best if shuffled first)
    for a in anchors:
        radius = random_centered(radius, 30) # Randomize the radius a bit for each point
        x, y = circle_points(x_center, y_center, radius, a)
        curveVertex(x, y)
        
        # Loop through all the points again for a weird effect
        for a in anchors:
            radius = random_centered(radius, 30) # Randomize the radius a bit for each point
            x, y = circle_points(0, 0, radius, a)
            curveVertex(x, y)

    # Run the curve through the starting three points to ensure smooth connection at the end
    curveVertex(x_0, y_0)
    curveVertex(x_1, y_1)
    curveVertex(x_2, y_2)
   
    
def random_list_value(val_list):
    # Returns a random value from a list
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value
        
        
def random_centered(value_og, offset=5):
    # Randomly varies value_og within the offset range
    value = random(value_og-offset, value_og+offset)
    return value

def circle_points(origin_x, origin_y, r=50, a=0):
    # Returns cartesian coordinates given a circle origin, radius, and angle
    x = origin_x + (r * cos(a))
    y = origin_y + (r * sin(a))
    return x, y


def range_float(start_val, end_val, inc_val):
    # Allows for similar functionality to built-in range() but with float step values
    start_val = float(start_val)
    end_val = float(end_val)
    inc_val = float(inc_val)

    count = int(math.ceil((end_val - start_val) / inc_val))

    L = [None,] * count

    L[0] = start_val
    for i in xrange(1,count):
        L[i] = L[i-1] + inc_val
    return L


