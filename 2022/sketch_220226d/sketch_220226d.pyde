# grid to draw LEON POLK SMITH   Untitled, 1945
# use b key to change colors
# p to save

cellSize = 20  # Size of cells
pause = True  # Pause
col = 1 # 1: black, 2: red, 3: orange, 4: white, 0: erase

def setup():
    global grid_w, grid_h
    global cells  # Array of cells
    global cellsBuffer  # Buffer while changing the others in the interations
    size(600, 600)

    # Instantiate arrays
    grid_w, grid_h = int(width / cellSize), int(height / cellSize)
    cells = [[None] * grid_w for _ in range(grid_h)]
    cellsBuffer = [[None] * grid_w for _ in range(grid_h)]   
    noFill()  
    background(200)  # Fill in black in case cells don't cover all the windows

def draw():
    
    background(209,57,57b)
    # Draw grid
    for x in range(grid_w):
        for y in range(grid_h):
            if cells[x][y] == 1:
                fill(30)
                stroke(30)
            elif cells[x][y] == 2: 
                fill(209,57,57)
                stroke(74,105,170)
            elif cells[x][y] == 3: 
                fill(255,229,121)
                stroke(255,229,121)
            elif cells[x][y] == 4: 
                fill(255)
                stroke(255)    
            else:
                noStroke()  # fill(dead)  # If dead
                noFill()        
            boxe(x * cellSize, y * cellSize, cellSize)

    # Create new cells manually on pause
    if pause and mousePressed:
        # Map and adef out of bound errors 
        # may need to adjsut mousexy due to grid size
        xCellOver = int(map(mouseX-10, 0, width, 0, width / cellSize))
        xCellOver = constrain(xCellOver, 0, width / cellSize - 1)
        yCellOver = int(map(mouseY-10, 0, height, 0, height / cellSize))
        yCellOver = constrain(yCellOver, 0, height / cellSize - 1)
        # Check against cells in buffer 
        if col == 0: 
            cells[xCellOver][yCellOver] = 0 
        elif col == 1:  
            cells[xCellOver][yCellOver] = 1  
        elif col == 2:  
            cells[xCellOver][yCellOver] = 2              
        elif col == 3:  
            cells[xCellOver][yCellOver] = 3                            
        elif col == 4:  
            cells[xCellOver][yCellOver] = 4      

    # And then save to buffer once mouse goes up
    elif pause and not mousePressed:
        # Save cells to buffer so we opeate with one array keeping the other intact
        for x in range(grid_w):
            for y in range(grid_h):
                cellsBuffer[x][y] = cells[x][y]

def boxe(x, y, r):
    with pushMatrix():
        translate(x+27, y+27)
        rotate(radians(45))  
        beginShape()
        for i in range(4):
            sx = cos(i * TWO_PI / 4) * r *.7 # adjust last digit to get gap btw squares
            sy = sin(i * TWO_PI / 4) * r *.7 # adjust last digit to get gap btw squares
            vertex(sx, sy)
        endShape(CLOSE)
            
def keyPressed():
    global col
    if key == 'p':  # save PNG
        saveFrame("#####.png")
    if key == 'b':  # blu
        col = col + 1
        if col > 4:
            col = 0
        print(col)
