def setup():
    size(1280,720)
    stroke(255)
    background(0)
    frameRate(120)
  
def draw():
    ellipse(mouseX, mouseY, min(abs(320-mouseX), abs(800-mouseX)), min(abs(160-mouseY), abs(500-mouseY)))
    line(640,320, mouseX, mouseY)
 

def mousePressed():
    clear()