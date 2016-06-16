add_library('sound')
#add_library('Minim')
#minim = Minim(this)

import os
path = os.getcwd()

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

class Game:
    def __init__ (self, w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.f = 0
        self.debugMode = False
        self.level = 1

        #self.music = Minim(this).loadFile(path+'/background.mp3')
        self.state = 'menu'        
    
    def loadStage(self):
        self.x = 0
        self.y = 0
        self.mario = Mario(100,200,self.g,50)
        self.platforms=[]
        self.enemies = []
        
        stage = open (path+'/level'+str(self.level))
        
        for line in stage:
            line = line.strip().split(',')
            
            if line[0] == 'p':
                self.platforms.append(Platform(int(line[1]),int(line[2]),int(line[3]),int(line[4])))
            elif line[0] == 's':
                self.enemies.append(SpongeBob(int(line[1]),int(line[2]),int(line[3]),int(line[4]), int(line[5]), int(line[6])))
            elif line[0] == 'music':
                self.music = SoundFile(this, path+'/'+line[1])
                self.music.amp(0.1)
                self.music.play()
            elif line[0] == 'bg':
                self.bgImg = loadImage(path+'/'+line[1])
            elif line[0] == 'stageEnd':
                print line[1]
                self.stageEnd = int(line[1])
                
    def display(self):
        stroke(255)
        
        #line(0,self.g,self.w,self.g)
        image(self.bgImg,0-game.x%game.w,0)
        image(self.bgImg,game.w-game.x%game.w,0)
     
        for p in self.platforms:
            p.display()
            
        for e in self.enemies:
            e.display()
            
        self.mario.display()

class Platform:
    def __init__ (self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def display(self):
        stroke(255)
        rect(self.x-game.x,self.y,self.w,self.h)
        
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
    
class SpongeBob (Creature):
    def __init__ (self,x,y,g,r,x1,x2):
        Creature.__init__ (self, x,y,g,r)
        self.img=loadImage(path+'/SB_walking.png')
        self.F = 6
        self.f = 0
        self.x1=x1
        self.x2=x2
        self.vx=1
        
    def update(self):
        if self.y+self.r < self.g:
            self.vy += 0.1
        else:
            self.vy = 0
            self.y = self.g-self.r
        
        if self.x >= self.x2:
            self.vx = -1
        elif self.x <= self.x1:
            self.vx = 1
        
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        self.update()
        
        if game.debugMode:
            fill (0)
            stroke(255)
            ellipse (self.x-game.x, self.y, 2*self.r, 2*self.r)
            stroke(255,0,0)
            line(self.x-self.r-game.x, self.g,self.x+self.r-game.x, self.g)
            
        self.f = self.f+0.1
                
        if self.vx > 0:
            image(self.img,self.x-self.r-game.x,self.y-self.r, self.r*2,self.r*2,int(self.f)%self.F*60,0,int(self.f)%self.F*60+60,59)
        else:
            image(self.img,self.x-self.r-game.x,self.y-self.r, self.r*2,self.r*2,int(self.f)%self.F*60+60,0,int(self.f)%self.F*60,59)

        
    
class Mario(Creature):
    def __init__ (self,x,y,g,r):
        Creature.__init__ (self, x,y,g,r)
        self.keyInput = {UP:False, DOWN: False, RIGHT:False,LEFT:False}
        self.img=loadImage(path+'/man.png')
        self.F = 8
        self.f = 0
        self.lastV=1
        self.jump = SoundFile(this, path+'/jump.mp3')
        
        
    def update(self):
        
        for e in game.enemies:
            if distance(self.x, self.y, e.x, e.y) <= self.r+e.r:
                if self.vy > 0 and self.y < e.y:
                    game.enemies.remove (e)
                    self.vy -= 8
                else:
                    game.music.stop()
                    game.__init__(800,600,500)
        
        onPlatform = False
        for p in game.platforms:

            if  p.x <= self.x <=p.x+p.w and self.y+self.r <= p.y+p.h and self.vy >= 0:
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
            #self.jump.play()
            
        self.x += self.vx
        self.y += self.vy
        
        if self.x-self.r < 0:
            self.x = self.r
        elif self.x+self.r > game.stageEnd:
            #self.x = game.stageEnd-self.r
            game.level+=1
            game.music.stop()
            game.loadStage()
    
        if self.x > game.w/2 and self.vx > 0 and self.x+self.r < game.stageEnd-game.w/2:
            game.x += self.vx
        elif game.x > 0 and self.vx < 0 and self.x+self.r < game.stageEnd-game.w/2:
            game.x += self.vx
    
    def display(self):
        self.update()
        
        if game.debugMode:
            fill (0)
            ellipse (self.x-game.x, self.y, 2*self.r, 2*self.r)
            stroke(255,0,0)
            line(self.x-self.r-game.x, self.g,self.x+self.r-game.x, self.g)
            
        if self.vx != 0:
            self.f = self.f+0.1
        else:
            self.f=0
                
        if self.lastV > 0:
            image(self.img,self.x-self.r-game.x,self.y-self.r, self.r*2,self.r*2,int(self.f)%self.F*153,0,int(self.f)%self.F*153+153,216)
        else:
            image(self.img,self.x-self.r-game.x,self.y-self.r, self.r*2,self.r*2,int(self.f)%self.F*153+153,0,int(self.f)%self.F*153,216)

game=Game(800,600,500)

def setup():
    size(game.w,game.h)
    background(0)
    path=os.getcwd()
    
def draw():
    background (0)
    
    if game.state == 'menu':
        background (0)
        #fill (0)
        #stroke(255)
        #rect(game.w/2-20,game.h/3-45,100,55)

        if game.w/2-20 < mouseX < game.w/2-20+100 and game.h/3-45 < mouseY < game.h/3-45+55:
            fill (255,0,0)
        else:
            fill (255)
        textSize(50)
        text ('Play', game.w/2-20, game.h/3)
        
    elif game.state == 'play':
        game.display()
    
def mousePressed():
    if game.state == 'menu':
        if game.w/2-20 < mouseX < game.w/2-20+100 and game.h/3-45 < mouseY < game.h/3-45+55:
            game.state='play'
            game.loadStage()

    
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