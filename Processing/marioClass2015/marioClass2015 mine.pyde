class Game:
    def __init__ (self, w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.mario = Mario(100,200,self.g,10)
        
    def display(self):
        stroke(255)
        line(0,self.g,self.w,self.g)
        self.mario.display()

class Creature:
    def __init__ (self, x,y,g,r):
        self.x=x
        self.y=y
        self.g=g
        self.r=r
        self.vx=0
        self.vy=0
        
    def update(self):
        if self.y+self.r < self.g:
            self.vy += 0.1
        else:
            self.vy = 0
            self.y = self.g-self.r
        
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        self.update()
        fill (0)
        ellipse (self.x, self.y, 2*self.r, 2*self.r)
    
class Mario(Creature):
    def __init__ (self,x,y,g,r):
        Creature.__init__ (self, x,y,g,r)
        self.keyInput = {UP:False, DOWN: False, RIGHT:False,LEFT:False}

    def update(self):
        if self.keyInput[LEFT]:
            self.vx = -2
        elif self.keyInput[RIGHT]:
            self.vx = 2
        else:
            self.vx = 0
            
        if self.y+self.r < self.g:
            self.vy += 0.1
        else:
            self.vy = 0
            self.y = self.g-self.r
        
        if self.keyInput[UP] and self.y == self.g-self.r:
            self.vy -= 6
            
        self.x += self.vx
        self.y += self.vy
        
game=Game(800,600,500)

def setup():
    size(game.w,game.h)
    background(0)
    
def draw():
    background (0)
    game.display()
    
def keyPressed():
    if keyCode == UP:
        game.mario.keyInput[UP]=True
    elif keyCode == LEFT:
        game.mario.keyInput[LEFT]=True
    elif keyCode == DOWN:
        game.mario.keyInput[DOWN]=True
    elif keyCode == RIGHT:
        game.mario.keyInput[RIGHT]=True
    
def keyReleased():
    if keyCode == UP:
        game.mario.keyInput[UP]=False
    elif keyCode == LEFT:
        game.mario.keyInput[LEFT]=False
    elif keyCode == DOWN:
        game.mario.keyInput[DOWN]=False
    elif keyCode == RIGHT:
        game.mario.keyInput[RIGHT]=False 