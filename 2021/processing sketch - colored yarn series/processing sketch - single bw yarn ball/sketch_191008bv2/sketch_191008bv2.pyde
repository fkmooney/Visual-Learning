################################################################################
# https://github.com/aaronpenne
################################################################################

import datetime
import string
import math
import sys
from random import shuffle, seed

import helper # file in folder

################################################################################
# Global variables
################################################################################

# Get time 
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Set random seed value for both Python 'random' and Processing 'random'
rand_seed = helper.get_seed('emptymonkey')
print(rand_seed)
# Comment out seeds below to get new shape on every run
seed(rand_seed) # This only applys to the Python random functions
randomSeed(rand_seed) # This only applys to the Processing random functions

# Parameters for draw speed
frame_rate = 10

# These globals are populated in setup()
anchors = []
len_anchors = 0

################################################################################
# Color palettes #FIXME need a library of these or something...
################################################################################

pal = [(0, 0, 0),  # bright salmon
       (0, 0, 0), # bright pink
       (0, 0, 0),  # yellow
       (00, 00, 100),  # salmon - controls fill, middle controls hue
       (0, 0, 0), # red
       ]

# Counter to allow for tracking draw() runs
count = 0

################################################################################
# Knobs to turn
################################################################################

# Canvas size
w = 4000  # width
h = 4000  # height

# Number of positions across canvas
x_grid_size = 4
y_grid_size = 4

# Center of each ball
x_pos = [x*w/x_grid_size for x in range(x_grid_size)]
y_pos = [y*h/y_grid_size for y in range(y_grid_size)]

# Size of empty space between edge and piece
x_pad = 2
y_pad = 2

# Number of points around individual circle, MAKES MROE COMPLEX
num_anchors = 60

# Radius of individual circle
r_mult = .99  # Decimal multiplier is pct of space to fill
if w > h:
    r_full = h/y_grid_size/2
else:
    r_full = w/x_grid_size/2
radius = r_full * r_mult 

# Size of lines
stroke_weight = 18



################################################################################
# setup() 
# function gets run once at start of program
################################################################################

def setup():
    # Sets size of canvas in pixels (must be first line)
    size(w, h) # (width, height)
    
    # Sets resolution dynamically (affects resolution of saved image)
    pixelDensity(displayDensity(2))  # 1 for low, 2 for high
    
    # Sets color space to Hue Saturation Brightness with max values of HSB respectively
    colorMode(HSB, 360, 100, 100, 100)
        
    # Set the number of frames per second to display
    frameRate(frame_rate)
    
    # Determine anchor points around circle for the curves to hit
    global anchors, len_anchors
    anchors = range_float(0+PI/2, TWO_PI+PI/2, TWO_PI/num_anchors)
    len_anchors = len(anchors)

    # Stops draw() from running in an infinite loop (should be last line)
    noLoop()  # Comment to run draw() infinitely (or until 'count' hits limit) 


################################################################################
# draw() 
# function gets run repeatedly (unless noLoop() called in setup())
################################################################################

def draw():
    curveTightness(0)
    
    # Loop counter to control number of draw() runs
    global count
    print(count)
    if count >= len_anchors-1:
        sys.exit(0)
    count += 1

    background(0,0,100)
        
    ################################################################################
    # Actual shape drawing begins
    ################################################################################
    for x in x_pos[x_pad:-x_pad+1]:
        for y in y_pos[y_pad:-y_pad+1]:
            print(x, y)
            # Aesthetics of lines
            noFill()
            #fill(*random_list_value(pal))
            
            p = random_list_value([0,1,2,3,4])
            fill(*pal[p])
            '''
            # Fill color based on probs
            p = random(0,1)
            if x < w/3:
                if p<0.5:
                    fill(*pal[3])
            elif x > 2*w/3:
                if p<0.5:
                    fill(*pal[3])
               
            if (x<w/5) or (x>4*w/5):
                if p<0.4:
                    continue
            elif (x<2*w/5) or (x>3*w/5):
                if p<0.2:
                    continue
            '''
            
            #noStroke()
            stroke(0)
            #stroke(*pal[0])
            strokeWeight(stroke_weight)
            
            draw_yarn_ball(x, y, radius)

    save_frame_timestamp('yarn', timestamp)
    
    # Save memory by closing image, just look at it in the file system
    if (w > 1000) or (h > 1000):
        exit()


################################################################################
# Functions
################################################################################

def draw_yarn_ball(x_center, y_center, radius):
    # Get three start/end points. The curve needs to retrace these 3 points to connect in a smooth loop 
    # https://forum.processing.org/two/discussion/14849/how-to-form-a-smooth-loop-using-curve
    beginShape()
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
        # radius = random_centered(radius, 30) # Randomize the radius a bit for each point
        x, y = circle_points(x_center, y_center, radius, a)
        curveVertex(x, y)
        
        # Loop through all the points again for a weird effect
        # for a in anchors:
        #     # radius = random_centered(radius, 30) # Randomize the radius a bit for each point
        #     x, y = circle_points(0, 0, radius, a)
        #     curveVertex(x, y)

    # Run the curve through the starting three points to ensure smooth connection at the end
    curveVertex(x_0, y_0)
    curveVertex(x_1, y_1)
    curveVertex(x_2, y_2)
    endShape()


def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    '''Saves each frame with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_{}_####.tif'.format(timestamp, filename, rand_seed))
    saveFrame(output_filename)
    print(output_filename)
    
    
def save_timestamp(filename, timestamp='', output_dir='output'):
    '''Saves image with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_####.tif'.format(timestamp, filename))
    save(output_filename)
    print(output_filename)
    
    
def random_list_value(val_list):
    '''Returns a random value from a list'''
    index = int(random(0, len(val_list)))
    value = val_list[index]
    return value
        
        
def random_centered(value_og, offset=5):
    '''Randomly varies value_og within the offset range'''
    value = random(value_og-offset, value_og+offset)
    return value


def random_gaussian_limit(min_val, max_val):
    '''Same as built-in randomGaussian but truncated to within a range'''
    new_val = max_val*randomGaussian()+min_val
    if new_val < min_val:
        new_val = min_val
    elif new_val > max_val:
        new_val = max_val
    return new_val


def circle_points(origin_x, origin_y, r=50, a=0):
    '''Returns cartesian coordinates given a circle origin, radius, and angle'''
    x = origin_x + (r * cos(a))
    y = origin_y + (r * sin(a))
    return x, y


def range_float(start_val, end_val, inc_val):
    '''
    Allows for similar functionality to built-in range() but with float step values
    Adapted from http://code.activestate.com/recipes/66472/
    '''
    start_val = float(start_val)
    end_val = float(end_val)
    inc_val = float(inc_val)

    count = int(math.ceil((end_val - start_val) / inc_val))

    L = [None,] * count

    L[0] = start_val
    for i in xrange(1,count):
        L[i] = L[i-1] + inc_val
    return L
