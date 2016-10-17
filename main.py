import pygame
from math3d import *
import math
import random
import time

#A basic healthbar class
class healthbar():
    def __init__(self,hearts):
        """
        :param hearts: The health of the input.
        """
        self.bars=hearts
        self.image=pygame.image.load("hearts.bmp").convert()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.x=0
        self.y=0
    def draw(self,window):
        """
        :param window: The surface the healthbar will be rendered onto.
        """
        index=0
        xmod=0
        while(self.bars-index>=1):
            window.blit(self.image.subsurface(0,0,16,16),(self.x+xmod,self.y))
            index+=1
            xmod+=16
        if self.bars-index!=0:
            window.blit(self.image.subsurface(32,0,16,16),(self.x+xmod,self.y))
        print(self.bars)
    def deal_damage(self):
        """
        :return: Returns the current health bar.
        """
        self.bars-=.5
        return self.bars
class player():
    def __init__(self):
        self.health=4
        self.pos=VectorN(20,20)
        self.radius=20
        self.dx=0
        self.dy=0
        self.fps=30
        self.spf=1/self.fps
        self.currentFrame=0
        self.image=pygame.image.load("link.png").convert()
        self.image.set_colorkey((self.image.get_at((0,0))))
        self.hit_time=0
        self.hit=False
        self.damaged=False
        self.bar=healthbar(self.health)
    def draw(self,window):
        x=self.pos[0]-16
        y=self.pos[1]-24
        if self.hit:
            self.image.set_alpha(128)
        elif not self.hit:
            self.image.set_alpha(255)
        pygame.draw.circle(window,(0,0,255),self.position().int(),20)
        window.blit(self.image.subsurface(32*self.currentFrame,0,32,48),(x,y))
        self.bar.draw(window)
    def update(self,x,y,elapsed):
        self.pos[0]=x
        self.pos[1]=y
        self.spf-=elapsed
        if self.spf<0:
            self.currentFrame+=1
            self.spf=1/self.fps
            if self.currentFrame>3:
                self.currentFrame=0
    def position(self):
        return VectorN(self.pos[0],self.pos[1])
    def intersects(self,distance,f_time):
        return f_time<1000 and f_time>0 and distance<self.radius
    def gethit(self):
        if self.hit_time>0:
            if self.damaged:
                self.damaged=False
                self.health=self.bar.deal_damage()
            self.hit_time-=elapsed
        elif self.hit_time<=0:
            self.hit=False
class tank():
    def __init__(self,player):
        self.image=pygame.image.load("turrets.png").subsurface(0,0,64,64)
        self.pos=VectorN(random.randint(50,550),random.randint(50,350))
        self.direction=random.randint(0,360)
        self.av=.03
        self.ray=None
        self.fire_interval=4000
        self.f_time=1000
        self.target=player
    def draw(self,window):
        rot=pygame.transform.rotate(self.image,self.direction-90)
        window.blit(rot,(self.pos[0]-rot.get_width()//2,self.pos[1]-rot.get_height()//2))
        pygame.draw.circle(window,(128,0,128),self.pos.int(),20)
        an=math.radians(360*((4000-self.fire_interval)/4000))
        pygame.draw.arc(window,(0,220,0),(self.pos[0]-16,self.pos[1]-16,32,32),0,an,7)
        if self.f_time<1000 and self.f_time>0:
            self.Ray.drawPygame(window,8,(123,123,123),800)
        self.Ray.draw_projection(self.target.position(),window)
    def update(self,elapsed):
        norm=VectorN(math.cos(math.radians(self.direction)),-math.sin(math.radians(self.direction)))
        self.Ray=Ray(self.pos,norm)
        an=norm.cross(self.target.position()-self.pos)[2]
        if an<0:
            self.av=.03
        elif an>0:
            self.av=-.03
        self.fire_interval-=elapsed
        if self.fire_interval<0:
            self.f_time-=elapsed
        if self.f_time<0:
            self.f_time=1000
            self.fire_interval=4000
        self.direction+=elapsed*self.av
        between=self.Ray.getDistanceToPoint(p.position())
        if between!=None and not self.target.hit and self.target.intersects(between,self.f_time):
            self.target.hit=True
            self.target.damaged=True
            self.target.hit_time=1000
#Initialization
pygame.init()
window=pygame.display.set_mode((640,480))
running=True
clk=pygame.time.Clock()
p=player()
tanks=[]
for num in range(0,2):
    tanks.append(tank(p))
while running:
    elapsed=clk.tick()
    #Events
    evt=pygame.event.poll()
    if evt.type==pygame.QUIT:
        running=False
        continue
    if evt.type==pygame.MOUSEMOTION:
        x,y=evt.pos
        p.update(x,y,elapsed)
    #Updating
    for t in tanks:
        t.update(elapsed)
    p.gethit()
    #Rendering
    window.fill((0,0,0))
    p.draw(window)
    for t in tanks:
        t.draw(window)
    pygame.display.flip()

#Exiting
pygame.quit()
