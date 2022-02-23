# https://www.sothebys.com/en/buy/auction/2019/important-prints-and-multiples-day-sale/leon-polk-smith-werkuebersicht-1946-1986
# werkübersicht 1946 -1986 - print no. 05, 1987

from random import choice

def setup():
    size(600,600)
    background(245)
    noLoop()
    
def draw():
    translate(-15,20)
    stroke(30)
    strokeWeight(50)
    line(200,-100,200,700)
    line(600,-100,600,700)
    
    lst = list(range(-12, 13))
    choice(lst)
    noStroke()
    fill(30)
    
    triangle(180, 50+choice(lst), 370, 0+choice(lst), 370, 100+choice(lst))
    triangle(180, 200+choice(lst), 370, 150+choice(lst), 370, 250+choice(lst))
    triangle(180, 350+choice(lst), 370, 300+choice(lst), 370, 400+choice(lst))
    triangle(180, 500+choice(lst), 370, 450+choice(lst), 370, 550+choice(lst))

    triangle(620, 50+choice(lst), 420, 0+choice(lst), 420, 100+choice(lst))
    triangle(620, 200+choice(lst), 420, 150+choice(lst), 420, 250+choice(lst))
    triangle(620, 350+choice(lst), 420, 300+choice(lst), 420, 400+choice(lst))
    triangle(620, 500+choice(lst), 420, 450+choice(lst), 420, 550+choice(lst))    
    
    triangle(220, 50+choice(lst), 50, 0+choice(lst), 50, 100+choice(lst))
    triangle(220, 200+choice(lst), 50, 150+choice(lst), 50, 250+choice(lst))
    triangle(220, 350+choice(lst), 50, 300+choice(lst), 50, 400+choice(lst))
    triangle(220, 500+choice(lst), 50, 450+choice(lst), 50, 550+choice(lst)) 
    
    saveFrame("output.png")
    
    
