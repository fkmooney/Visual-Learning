w, h = 600, 600
subdivisions = 7
min_diff = 100 # Not too small
sep = 0 # Space between quads
splits = [.5, 1, 1.5] # Subdivision adjustment
edge = 0 # Canvas Border

def setup():
    size(w, h)    
    background(255)
    stroke(30)
    strokeWeight(8)
    
    quads = []
    # Add the initial rectangle
    quads.append([(edge, edge), (w - edge, edge), (w - edge, h - edge), (edge, h - edge)])
    
    # Start splitting things up
    for i in range(subdivisions):
        q_index = int(random(len(quads)))
        q = quads[q_index]
        q_lx = q[0][0]
        q_rx = q[1][0]
        q_ty = q[0][1]
        q_by = q[2][1]
        
        s = splits[int(random(len(splits)))]
        if (random(1) < .5):
            if ((q_rx - q_lx) > min_diff):
                # Get new shapes x value (y is same)
                x_split = (q_rx - q_lx)/2 * s + q_lx
                
                quads.pop(q_index)
                quads.append([(q_lx, q_ty), (x_split - sep, q_ty), (x_split - sep, q_by), (q_lx, q_by)])
                quads.append([(x_split + sep, q_ty), (q_rx, q_ty), (q_rx, q_by), (x_split + sep, q_by)])
                        
        else:
            if ((q_by - q_ty) > min_diff):
                y_split = (q_by - q_ty)/2 * s + q_ty
                
                quads.pop(q_index)
                quads.append([(q_lx, q_ty), (q_rx, q_ty), (q_rx, y_split - sep), (q_lx, y_split - sep)])
                quads.append([(q_lx, y_split + sep), (q_rx, y_split + sep), (q_rx, q_by), (q_lx, q_by)])
            
    redq = int(random(0,4))
    yellowq = int(random(0,4))
    blueq = int(random(0,4))
    quad_dig = [0,1,2,3]
        
    for q in quads:
        
        if len(quad_dig) > 0:
            q_dig = quad_dig.pop()
        
            if q_dig == redq:
                fill(255,0,0)
            elif q_dig == yellowq:
                fill(255,255,0)
            elif q_dig == blueq:
                fill(0,0,255)
            else:
                fill(255)
            
        beginShape()
        for p in q:
            vertex(p)
        endShape(CLOSE)

def draw():
    b=1

def keyPressed():
    saveFrame("output.png")
