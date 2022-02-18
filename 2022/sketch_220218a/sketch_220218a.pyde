# inspired by Dan Graham Scheme for Magazine Page 'Adertisement' (1965)

def setup():
    size(600,600)
    background(245) 
    
def draw():

    noFill()
    stroke(30)
    strokeWeight(2)
    rect(10, 10, width-(2*10), height-(2*10))

    fill(30)
    for y in range(25,590,16):
        price = random(00.07,02.51)        
        text('A       {:.2f}'.format(price), 280, y)

    noLoop()
    saveFrame("output.png")
