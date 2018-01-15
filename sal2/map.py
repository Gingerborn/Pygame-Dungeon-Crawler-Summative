from settings import *
import pygame as pg

def collide_hit_rect(one,two):
    return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self,filename):
        self.data = []
        with open(filename,'rt') as f:
            for line in f:
                self.data.append(line.strip())
        
        self.TILEWIDTH = len(self.data[0])
        self.TILEHEIGHT = len(self.data)
        self.WIDTH = self.TILEWIDTH * TILESIZE
        self.HEIGHT = self.TILEHEIGHT * TILESIZE


class Camera:
    def __init__(self,wc,hc):
        self.camera = pg.Rect(0,0,wc,hc)
        self.WIDTH = wc
        self.HEIGHT = hc
        
    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self,target):
        x = -target.rect.centerx + int(WIDTH/2)
        y = -target.rect.centery + int(HEIGHT/2)
        
##        scrolling limit
        x= min(0,x)#left
        y = min(0,y)#top
        x = max(-(self.WIDTH - WIDTH), x)#right
        y = max(-(self.HEIGHT - HEIGHT),y)#bottom
        self.camera = pg.Rect(x,y,self.WIDTH,self.HEIGHT)