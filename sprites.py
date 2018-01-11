#sprite classes for platform

from settings import *
import pygame as pg
import os
import time
vec = pg.math.Vector2



class Player(pg.sprite.Sprite):
    def __init__(self,folder):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(folder,'RS.png')).convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.frame = 0
        self.stand_timer = 10
        self.walk_timer = 0
        self.folder = folder

## STAND TIMER STARTS AT 5 AND WALK TIMER STARTS COUNTING UP BY 1, ONCE IT REACHES 5 STAND TIMER IS SET
## TO 0 AND THEN IT STARTS GOING UP BY 1, AND THE STATE AT WHICH EITHER TIMER IS IN DICTATES WHICH
## FRAME WILL BE CALLED, IF STAND TIMER IS AT 5, THEN FRAME 0 OR 3 WILL BE CALLED DEPENDING ON WHICH
## KEY IS BEING PUSHED DOWN, LEFT OR RIGHT (IT LOOKS LIKE A BUNCH OF TRASH BUT HEY! THE TRASH WORKS!)

    def flip(self):
        if self.frame == 0:
            if self.walk_timer >= 10:
                self.stand_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'RS.png')).convert()
            self.image.set_colorkey(WHITE)
        if self.frame == 1:
            if self.walk_timer >= 10:
                self.stand_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'LS.png')).convert()
            self.image.set_colorkey(WHITE)
        if self.frame == 2:
            if self.stand_timer >= 10:
                self.walk_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'RW.png')).convert()
            self.image.set_colorkey(WHITE)
        if self.frame == 3:
            if self.stand_timer >= 10:
                self.walk_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'LW.png')).convert()
            self.image.set_colorkey(WHITE)
        if self.frame == 4:
            if self.walk_timer >= 10:
                self.stand_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'UL.png')).convert()
            self.image.set_colorkey(WHITE)
        if self.frame == 5:
            if self.stand_timer >= 10:
                self.walk_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'UR.png')).convert()
            self.image.set_colorkey(WHITE)
        if self.frame == 6:
            if self.walk_timer >= 10:
                self.stand_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'DL.png')).convert()
            self.image.set_colorkey(WHITE)
        if self.frame == 7:
            if self.stand_timer >= 10:
                self.walk_timer = 0
            self.image = pg.image.load(os.path.join(self.folder,'DR.png')).convert()
            self.image.set_colorkey(WHITE)
            
    def update(self):
        self.flip()
        self.acc = vec(0,0)
        keys = pg.key.get_pressed()
        # left
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 1
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 3
                self.stand_timer += 1
        # right
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 0
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 2
                self.stand_timer += 1
        #up
        if keys[pg.K_UP]:
            self.acc.y = -PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 4
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 5
                self.stand_timer += 1
        #down
        if keys[pg.K_DOWN]:
            self.acc.y = PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 6
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 7
                self.stand_timer += 1
            
        # wrap around the sides of the screen   
        if self.pos.x > WIDTH - 15:
            self.acc = vec(0,0)
            self.vel = vec(0,0)
            self.pos.x -= 0.1
        if self.pos.x < 15:
            self.acc = vec(0,0)
            self.vel = vec(0,0)
            self.pos.x += 0.1
        if self.pos.y > HEIGHT - 20:
            self.acc = vec(0,0)
            self.vel = vec(0,0)
            self.pos.y -= 0.1
        if self.pos.y < 20:
            self.acc = vec(0,0)
            self.vel = vec(0,0)
            self.pos.y += 0.1
        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        
      

        self.rect.center = self.pos
