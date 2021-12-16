# testing putting fonts into composition

def setup():
    size(500, 700)
    background(229,230,50)

def draw():  
    rotate(radians(-45))
        
    # adding a rect for composition
    fill(255)
    noStroke()
    rect(-200,200,450,450)
    
    # add a font and text
    font = createFont("Helvetica-Bold.ttf", 120)
    textFont(font)
    fill(0)
    text("the", -190,300) # text and position
    text("cramps", -190,380) # text and position
    
    # add another font and text
    font = createFont("Helvetica-Bold.ttf", 20)
    textFont(font)
    text("with specil guests", -120,425) # text and position
    text("pale face of youth", -120,450) # text and position

        # add another font and text
    font = createFont("Helvetica.ttf", 12)
    textFont(font)
    text("at the peppermint lounge", -190,500) # text and position
    text("100 fifth ave, new york city", -190,520) # text and position
    text("saturday June 4 1983", -190,550) # text and position
    text("no age limit / $10", -190,570) # text and position
    
def keyPressed():
    saveFrame('####.png')

    
