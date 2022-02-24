# https://www.invaluable.com/auction-lot/smith-leon-polk-werkuebersicht-1949-1987-1596-c-ec447ada0f

from random import choice

def setup():
    size(600,600)
    background(245,60,100)
    noLoop()
    
def draw():

    lst = list(range(-8, 8))
    noStroke()
    fill(30)
    
    #center shapes
    beginShape()
    vertex(300+choice(lst),100)
    vertex(350+choice(lst),100)
    vertex(350+choice(lst),200)
    vertex(300,200)
    endShape(CLOSE)
    
    beginShape()
    vertex(300,200)
    vertex(250+choice(lst),200)
    vertex(250+choice(lst),300)
    vertex(300,300)
    endShape(CLOSE)   

    beginShape()
    vertex(300,300)
    vertex(350+choice(lst),300)
    vertex(350+choice(lst),400)
    vertex(300,400)
    endShape(CLOSE) 
    
    beginShape()
    vertex(300,400)
    vertex(250+choice(lst),400)
    vertex(250+choice(lst),500)
    vertex(300,500)
    endShape(CLOSE) 
    
    # edge shapes
    beginShape()
    vertex(200+choice(lst),200)
    vertex(150,200)
    vertex(150,300)
    vertex(200+choice(lst),300)
    endShape(CLOSE)  
    
    beginShape()
    vertex(400+choice(lst),300)
    vertex(450,300)
    vertex(450,400)
    vertex(400+choice(lst),400)
    endShape(CLOSE) 
    
    beginShape()
    vertex(400+choice(lst),100)
    vertex(450+choice(lst),100)
    vertex(450+choice(lst),200)
    vertex(400,200)
    endShape(CLOSE)
 
    beginShape()
    vertex(200+choice(lst),400)
    vertex(150+choice(lst),400)
    vertex(150+choice(lst),500)
    vertex(200,500)
    endShape(CLOSE)       
    
    noFill()
    stroke(245)
    strokeWeight(300)
    circle(300,300,600)
    
    fill(30)
    textSize(4)
    text("""
# smith-leon-polk werkuebersicht-1949-1987-1596-c

from random import choice

def setup():
    size(600,600)
    background(245,60,100)
    noLoop()
    
def draw():

    lst = list(range(-8, 8))
    noStroke()
    fill(30)
    
    #center shapes
    beginShape()
    vertex(300+choice(lst),100)
    vertex(350+choice(lst),100)
    vertex(350+choice(lst),200)
    vertex(300,200)
    endShape(CLOSE)
    
    beginShape()
    vertex(300,200)
    vertex(250+choice(lst),200)
    vertex(250+choice(lst),300)
    vertex(300,300)
    endShape(CLOSE)   

    beginShape()
    vertex(300,300)
    vertex(350+choice(lst),300)
    vertex(350+choice(lst),400)
    vertex(300,400)
    endShape(CLOSE) 
    
    beginShape()
    vertex(300,400)
    vertex(250+choice(lst),400)
    vertex(250+choice(lst),500)
    vertex(300,500)
    endShape(CLOSE) 
    
    # edge shapes
    beginShape()
    vertex(200+choice(lst),200)
    vertex(150,200)
    vertex(150,300)
    vertex(200+choice(lst),300)
    endShape(CLOSE)  
    
    beginShape()
    vertex(400+choice(lst),300)
    vertex(450,300)
    vertex(450,400)
    vertex(400+choice(lst),400)
    endShape(CLOSE) 
    
    beginShape()
    vertex(400+choice(lst),100)
    vertex(450+choice(lst),100)
    vertex(450+choice(lst),200)
    vertex(400,200)
    endShape(CLOSE)
 
    beginShape()
    vertex(200+choice(lst),400)
    vertex(150+choice(lst),400)
    vertex(150+choice(lst),500)
    vertex(200,500)
    endShape(CLOSE)       
    
    noFill()
    stroke(30)
    strokeWeight(300)
    circle(300,300,600)
    """
    , 10, 10)
    
    saveFrame("output.png")
    
    
