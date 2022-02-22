# https://www.google.com/search?q=dan+flavin+drawings&rlz=1C1GCEB_enUS846US846&sxsrf=APq-WBv-2BlSGb3F11RrfV2OncJUDhKJrQ:1645495484545&source=lnms&tbm=isch&sa=X&sqi=2&ved=2ahUKEwigs9eunJL2AhUpzIUKHfmtAL0Q_AUoAXoECAIQAw&biw=1366&bih=625&dpr=1#imgrc=RM3eHI0T6jz8_M

def setup():
    size(600,600)
    background(245)
    noLoop()
    
def draw():
    
    stroke(30)
    strokeWeight(1)
    
    line(300,0,300,400)
    line(300,400,0,500)
    line(300,400,600,500)
    
    for x in range(170,470,50):
        fill(245)
        if x < 300:
            stroke(0,0,255,100)
        else:
            stroke(0,200,0,100)
        rect(x,100,10,350)
        
    for y in range(145,445,50):
        stroke(180)
        if y < 250:
            fill(255,80,100,)
        else:
            fill(255,250,100,)
        rect(125,y,350,10)
    
    saveFrame("output.png")
    
    
