x = 210
def setup():
    size(600,400)
    background(  30, 144, 255)
def draw():
    global x
    push()
    fill(178, 34, 34)
    rect(150,180,50,200)
    pop()
    push()
    fill(178, 34, 34)
    rect(0,180,50,200)
    pop()
    push()
    fill(  255, 215, 0)
    rect(190,350,40,350)
    rect(230,370,60,20)
    rect(280,350,10,20)
    rect(260,340,10,30)
    pop()
    push()
    fill(  30, 144, 255)
    rect(195,355,30,40)
    fill(240, 230, 140)
    rect(50,20,100,130)
    pop()
    push()
    fill(178, 34, 34)
    rect(80,150,40,50)
    rect(50,180,100,180)
    pop()
    push()
    triangle(90,70,90,100,x,85)
    fill(0, 0, 0)
    ellipse(100,120,40,40)
    pop()
    push()
    strokeWeight(10)
    point (80,70)
    point (110,65)
    point(100,190)
    point(100,210)
    point(100,240)
    point(100,270)
    point(100,300)
    pop()
    x += 5
