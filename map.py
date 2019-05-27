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
        
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * tilesize
        self.height = self.tileheight * tilesize


class Camera:
    def __init__(self,wc,hc):
        self.camera = pg.Rect(0,0,wc,hc)
        self.width = wc
        self.height = hc
        
    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self,target):
        x = -target.rect.centerx + int(width/2)
        y = -target.rect.centery + int(height/2)
        
##        scrolling limit
        x= min(0,x)#left
        y = min(0,y)#top
        x = max(-(self.width - width), x)#right
        y = max(-(self.height - height),y)#bottom
        self.camera = pg.Rect(x,y,self.width,self.height)