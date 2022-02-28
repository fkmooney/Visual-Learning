# inspired by John Baldassari's I will Not make Any More Boring Art (1971)

def setup():
    size(600,600)
    background(245) 
    noLoop()
        
def draw():

    fill(30)
    textSize(5)
    for y in range(18,590,8): 
        for x in range(15,590, 97):     
            text("I will not make any more boring art. ", x, y)
    saveFrame("output.png")
