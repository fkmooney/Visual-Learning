def setup():
    background(220)
    size(600,600)
    stroke(245)
    strokeWeight(50)
    noFill()
    square(0,0,600)
    
    translate(0,70)
    
    font = createFont("Montserrat-Black.otf", 42)
    font2 = createFont("Montserrat-Medium.otf", 35)
    textFont(font)
    fill(30)
    text("ETIQUETTE DU MONDE", 43, 140)
    
    textFont(font2)
    text("ETIQUETTE MAGIC NO. 1", 85, 260)
    text("DE KEMPTON MOONEY",87, 300)
    text("- 22 02 2022 -", 183, 340)
    text("HOMMAGE A MANZONI", 85, 380)
    
    saveFrame("output.png")
    

    
    
