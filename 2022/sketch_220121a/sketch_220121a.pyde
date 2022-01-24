def setup():
    size(600, 600)
    background(245)
    strokeWeight(3)
    stroke(30)

def draw():
    background(245)

    spacing = 20
    col_width = width

    lines_row_spacing = 10
    number_of_lines = (width - 100) / lines_row_spacing
    line_spacing = 5
    line_size = 30

    x_offset = line_size/2
    col_x_range = [x_offset + (2 * spacing), x_offset + (col_width - 2 * spacing)]

    col_size = col_x_range[1] - col_x_range[0]

    lines_per_col = range(col_x_range[0], col_x_range[1], line_size + line_spacing)
    for i, x in enumerate(lines_per_col):

        lines_num = range(number_of_lines)
        for j in lines_num:
            y = 50 + j * lines_row_spacing

            angle = map(j, lines_num[0], lines_num[-1], 0, 360)
                    
            with pushMatrix():
                translate(y, x)
                rotate(radians(angle*1-90))
                line(0, 0, line_size, 0)

    noLoop()

def keyPressed():
    saveFrame("output.png")
