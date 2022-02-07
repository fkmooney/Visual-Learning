def setup():
    size(600,600)
    background(225,0,0) 
    
def draw():

    fill(255)
    noStroke()
    rect(35, 60, width-(2*35), 85+(2*5))
    rect(70, 180, width-(2*70), 85+(2*5))
    rect(110, 300, width-(2*110), 85+(2*10))
    rect(50, 430, width-(2*50), 85+(2*5))
    
    font = createFont("Montserrat-BlackItalic.otf", 85)
    textFont(font)
    fill(30)
    text("We are the", 43, 140)
    text("slaves of", 90, 260)
    text("objects",130, 380)
    text("around us", 70, 510)

    noLoop()
    saveFrame("output.png")
