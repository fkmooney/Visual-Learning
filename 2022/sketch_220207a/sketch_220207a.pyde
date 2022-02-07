# inspired by Sopit Taeuber-Arp's Hasuer & Wirth
def setup():
    size(600,600)
    background(30)
    
def draw():
    noStroke()
    fill(245)
    circle(50,50,60)
    fill(0,120,235)
    circle(120,50,60)
    circle(190,50,60)
    fill(245)
    rect(230,60,120,60)
    
    circle(430,50,60)
    circle(500,50,60)
    circle(430,120,60)
    circle(500,120,60)
    circle(430,190,60)
    circle(430,260,60)
    fill(255,50,0)
    rect(500,170,70,85)
    
    fill(245)
    circle(360,500,60)
    circle(430,500,60)
    rect(475,450,120,60)
    
    rect(5,300,120,60)
    circle(180,410,60)
    
    rect(40,410,60,20)
    rect(40,450,60,20)
    rect(40,490,60,20)
    rect(40,530,60,20)
    
    fill(180,180,180)
    rect(200,250,60,90)
    
    noFill()
    stroke(245)
    strokeWeight(1)
    square(5,5,width-10)
    
    noLoop()
    saveFrame("output.png")
