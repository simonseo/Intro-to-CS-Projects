import os
path = os.getcwd()

class Game:
    def __init__ (self, w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.mario = Mario(100,200,self.g,50)
        self.platforms=[]
        self.platforms.append(Platform(200,300,100,10))
        self.platforms.append(Platform(200,400,100,10))
        self.platforms.append(Platform(400,300,100,10))
        
        
    def display(self):
        stroke(255)
        line(0,self.g,self.w,self.g)
        
        for p in self.platforms:
            p.display()
            
        self.mario.display()

class Platform:
    def __init__ (self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def display(self):
        stroke(255)
        rect(self.x,self.y,self.w,self.h)
        
        
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
        self.img=loadImage(path+'/man.png')
        self.F = 8
        self.f = 0
        self.lastV=1
        
        
    def update(self):
        onPlatform = False
        for p in game.platforms:
            print self.y+self.r, self.g, p.y

            if  p.x <= self.x <=p.x+p.w and self.y+self.r <= p.y+p.h and self.vy > 0:
                self.g = p.y
                onPlatform = True
                break
        
        if not onPlatform:
            self.g = game.g
        
        if self.keyInput[LEFT]:
            self.vx = -2
            self.lastV = -1
        elif self.keyInput[RIGHT]:
            self.vx = 2
            self.lastV = 1
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
    
    def display(self):
        self.update()
        fill (0)
        ellipse (self.x, self.y, 2*self.r, 2*self.r)
        stroke(255,0,0)
        line(self.x-self.r, self.g,self.x+self.r, self.g)
        if self.vx != 0:
            self.f = self.f+0.1
        else:
            self.f=0
                
        if self.lastV > 0:
            image(self.img,self.x-self.r,self.y-self.r, self.r*2,self.r*2,int(self.f)%self.F*153,0,int(self.f)%self.F*153+153,216)
        else:
            image(self.img,self.x-self.r,self.y-self.r, self.r*2,self.r*2,int(self.f)%self.F*153+153,0,int(self.f)%self.F*153,216)

game=Game(800,600,500)

def setup():
    size(game.w,game.h)
    background(0)
    path=os.getcwd()
    
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