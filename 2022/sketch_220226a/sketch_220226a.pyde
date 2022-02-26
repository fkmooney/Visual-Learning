# How likely for a cell to be alive at start (in percentage)
probabilityOfAliveAtStart = 45
cellSize = 20  # Size of cells
# Variables for timer
interval = 100
lastRecordedTime = 0

def setup():
    frameRate(10)
    global grid_w, grid_h
    global cells  # Array of cells
    global cellsBuffer  # Buffer while changing the others in the interations
    size(600, 600)
    # Instantiate arrays
    grid_w, grid_h = int(width / cellSize), int(height / cellSize)
    cells = [[None] * grid_w for _ in range(grid_h)]
    cellsBuffer = [[None] * grid_w for _ in range(grid_h)]
    # This stroke will draw the background grid
    noFill() 
    # Initialization of cells
    for x in range(grid_w):
        for y in range(grid_h):
            state = random(100)
            if state > probabilityOfAliveAtStart:
                state = 0
            else:
                state = 1
            cells[x][y] = state  # Save state of each cell
    background(245)  # Fill in black in case cells don't cover all the windows

def draw():
    background(245)
    global lastRecordedTime
    # Draw grid
    for x in range(grid_w):
        for y in range(grid_h):
            if cells[x][y] == 1:
                n = calc_neighbours(x, y)
                stroke(30)  # If alive
                fill(30)
            else:
                noStroke()  # fill(dead)  # If dead
                noFill()
            squaree(x * cellSize, y * cellSize, cellSize)
    # Iterate if timer ticks
    if millis() - lastRecordedTime > interval:
        iteration()
        lastRecordedTime = millis()
    # Create new cells manually on pause
    if mousePressed:
        # Map and adef out of bound errors
        xCellOver = int(map(mouseX, 0, width, 0, width / cellSize))
        xCellOver = constrain(xCellOver, 0, width / cellSize - 1)
        yCellOver = int(map(mouseY, 0, height, 0, height / cellSize))
        yCellOver = constrain(yCellOver, 0, height / cellSize - 1)
        # Check against cells in buffer
        if cellsBuffer[xCellOver][yCellOver] == 1:  # Cell is alive
            cells[xCellOver][yCellOver] = 0  # Kill
        else:  # Cell is dead
            cells[xCellOver][yCellOver] = 1  # Make alive
    # And then save to buffer once mouse goes up
    elif not mousePressed:
        # Save cells to bufferso we opeate with one array keeping the other intact
        for x in range(grid_w):
            for y in range(grid_h):
                cellsBuffer[x][y] = cells[x][y]

def iteration():  # When the clock ticks
    # Save cells to buffer
    # (so we opeate with one array keeping the other intact)
    for x in range(grid_w):
        for y in range(grid_h):
            cellsBuffer[x][y] = cells[x][y]
    # Visit each cell:
    for x in range(grid_w):
        for y in range(grid_h):
            # And visit all the neighbours of each cell
            neighbours = calc_neighbours(x, y)
            if cellsBuffer[x][y] == 1:
                if neighbours < 2 or neighbours > 3:
                    cells[x][y] = 0  # Die unless it has 2 or 3 neighbours
            else:  # The cell is dead: make it live if necessary
                if neighbours == 3:
                    cells[x][y] = 1  # Only if it has 3 neighbours

def calc_neighbours(x, y):
    neighbours = 0  # We'll count the neighbours
    for xx in range(x - 1, x + 2):
        for yy in range(y - 1, y + 2):
                    # Make sure you are not out of bounds
            if 0 <= xx < grid_w and 0 <= yy < grid_w:
                # Make sure to check against self
                if not (xx == x and yy == y):
                    if cellsBuffer[xx][yy] == 1:
                        # Check alive neighbours and count them
                        neighbours = neighbours + 1
    return neighbours

def keyPressed():
    if key == 'p':  # save PNG
        saveFrame("####.png")

def squaree(x, y, r):
    with pushMatrix():
        translate(x+10, y+10) # use to center after cell size change
        rotate(radians(45))
        beginShape()
        for i in range(4):
            sx = cos(i * TWO_PI / 4) * r * 0.6
            sy = sin(i * TWO_PI / 4) * r * 0.6
            vertex(sx, sy)
        endShape(CLOSE)
