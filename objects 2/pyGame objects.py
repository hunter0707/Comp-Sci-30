import pygame, sys, random
import pygame.locals as gg #gameglobals
import math

ww = 1200
wh = 800
window = pygame.display.set_mode((ww,wh))
pygame.init()
clock = pygame.time.Clock()

class rectangle:
    def __init__(self):
        self.w = random.randint(50,100)
        self.h = random.randint(50,100)
        self.xpos = random.randint(self.w,ww-self.w) #spawn
        self.ypos = random.randint(self.h,wh-self.h)
        self.m = (self.w*self.h)/2500
        self.xd = math.sqrt(50/self.m)
        print(self.w,self.h,self.xd)
        self.yd = self.xd * random.choice([-1,1]) #random y dir, but same speed as x
        self.xd *= random.choice([-1,1]) #random x dir
        self.color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.a = 0
        self.b = 0
        self.rect = pygame.Rect(self.xpos,self.ypos,self.w,self.h)
        self.go = True
    def draw(self):
        self.pos = self.xpos,self.ypos,self.w,self.h
        pygame.draw.rect(window,self.color,self.pos)
    def getrect(self):
        return pygame.Rect(self.xpos,self.ypos,self.w,self.h)
    def move(self):
        if self.xpos >= ww - self.w or self.xpos <= self.a:
            self.xd *= -1 #direction change at window edge
        if self.ypos >= wh - self.h or self.ypos <= self.b:
            self.yd *= -1 #direction change at window edge
        self.xpos += self.xd
        self.ypos += self.yd
    def switch(self,d,i): #free bounce and no energy transfer
        if d == 'x':
            self.xd *= -1
        elif d == 'y':
            self.yd *= -1
    def collide(self):
        for i in objs:
            if self.getrect().colliderect(i.getrect()) == 1 and (self.getrect().width != i.getrect().width or self.getrect().height != i.getrect().height): #collides and not same rect
            #if (self.ypos > i.ypos and self.ypos < i.ypos + i.h) or (self.ypos + self.h < i.ypos + i.h and i.ypos > self.ypos):
                #(8 is max velocity so rectangles can get 16 deep into each other)
                if i == objs[-1]: #stops player obj if touching
                    i.go = False
                else:
                    objs[-1].go = True #lets player obj go if not touching
                if self.xd < 0 and self.xpos < i.xpos + i.w and self.xpos > i.xpos + i.w - 16: #self is moving left, self left between i right and i right - 16 
                    self.switch('x',i)
                elif self.xd > 0 and self.xpos + self.w > i.xpos and self.xpos + self.w < i.xpos + 16: #self is moving right, right between i left and left + 16
                    self.switch('x',i)
            #else:
                if self.yd < 0 and self.ypos < i.ypos + i.h and self.ypos > i.ypos + i.h - 16:
                    self.switch('y',i)
                elif self.yd > 0 and self.ypos + self.h > i.ypos and self.ypos + self.h < i.ypos + 16:
                    self.switch('y',i)

class erect(rectangle): #elastic collision with energy transfers
    def __init__(self):
        rectangle.__init__(self)
    def switch(self,d,i):
        if d == 'x':
            self.xd *= -1
            #self.xd = ((self.m-i.m)/(self.m+i.m))*self.xd + ((2*i.m)/(self.m+i.m))*i.xd
            print(self.xd)
        elif d == 'y':
            self.yd *= -1
            #self.yd = ((self.m-i.m)/(self.m+i.m))*self.yd + ((2*i.m)/(self.m+i.m))*i.yd
            print(self.yd)

class circle(rectangle):
    def __init__(self):
        rectangle.__init__(self)
        self.w = random.randint(25,50)
        self.h = self.w
        self.a = self.w
        self.b = self.a
    def draw(self):
        pygame.draw.circle(window,self.color,[round(self.xpos),round(self.ypos)],self.w)

class player(rectangle):
    def __init__(self):
        rectangle.__init__(self)
        self.w = 50
        self.h = 50
        self.v = 10
        self.xpos = (ww - self.w)/2
        self.ypos = wh/2
        self.r = 255
        self.g = 0
        self.b = 0
        self.stage = 0
        self.go = True
        self.m = 1
        print('this is player')
    def draw(self):
        d = 5
        stage = self.stage
        #the following if/else statement cycles through the RGB column
        #there's probably/definitely a more elegant solution but it works so i'm ok with it. will probably rewrite later.
        if stage == 0:
            self.b += d
            if self.b == 255:
                stage = 1
        elif stage == 1:
            self.r -= d
            if self.r == 0:
                stage = 2
        elif stage == 2:
            self.g += d
            if self.g == 255:
                stage = 3
        elif stage == 3:
            self.b -= d
            if self.b == 0:
                stage = 4
        elif stage == 4:
            self.r += d
            if self.r == 255:
                stage = 5
        elif stage == 5:
            self.g -= d
            if self.g == 0:
                stage = 0

        self.stage = stage #sets the stage

        self.color = pygame.Color(self.r,self.g,self.b)
        self.pos = (self.xpos,self.ypos,self.w,self.h)
        pygame.draw.rect(window,self.color,self.pos)
    def move(self):
        keys = pygame.key.get_pressed()
        keys = {'up':keys[pygame.K_UP],'down':keys[pygame.K_DOWN],'left':keys[pygame.K_LEFT],'right':keys[pygame.K_RIGHT]}
        if self.go:
            if self.xpos <= ww - self.w and self.xpos >= 0:
                if keys['left']:
                    self.xpos -= self.v
                if keys['right']:
                    self.xpos += self.v
            elif self.xpos > ww - self.w:
                self.xpos -= self.v
            elif self.xpos < 0:
                self.xpos += self.v

            if self.ypos <= wh - self.h and self.ypos >= 0:
                if keys['up']:
                    self.ypos -= self.v
                if keys['down']:
                    self.ypos += self.v
            elif self.ypos > wh - self.h:
                self.ypos -= self.v
            elif self.ypos < 0:
                self.ypos += self.v


#shapes = [random.choice([circle(),rectangle()]) for i in range(10)]
player1 = player()
objs = [erect() for i in range(3)]
objs.append(player1)
rect = [i.rect for i in objs] #rect object for each obj, used for collisions

while True:
    window.fill(pygame.Color(0,0,0))
    for i in objs:
        i.draw()
        i.move()    
        i.collide()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == gg.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)