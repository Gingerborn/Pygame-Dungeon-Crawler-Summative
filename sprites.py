#sprite classes for platform

from settings import *
import pygame as pg
import os
import time

from random import uniform
from map import collide_hit_rect

vec = pg.math.Vector2


def collide_with_walls(sprite,group,dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width/2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width/2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite,group,False,collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height/2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height/2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


class Player(pg.sprite.Sprite):
    def __init__(self,folder,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.image.load(os.path.join(folder,'RS.png')).convert()
        self.image.set_colorkey(WHITE)
        self.image2 = game.player_img2
        self.rect = self.image.get_rect()
        self.hit_rect = player_hit_rect
        self.hit_rect.center = self.rect.center
##        self.rect.center = (WIDTH/2,HEIGHT / 2)
        self.pos = vec(x,y)*TILESIZE
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.frame = 0
        self.stand_timer = 10
        self.walk_timer = 0
        now = pg.time.get_ticks()
        self.last_shot = now
        self.folder = folder
        self.rot = 0
        
##        self.groups = game.all_sprites
##        pg.sprite.Sprite.__init__(self,self.groups)
##        self.game = game
##        self.rect = self.image.get_rect()
##        self.hit_rect = player_hit_rect
##        self.hit_rect.center = self.rect.center
##        self.vel = vec(0,0)
##        self.pos = vec(x,y)*tilesize
##        self.rot = 0
##        self.last_shot = 0

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
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self,self.game.walls,'y')
        self.rect.center = self.hit_rect.center
        keys = pg.key.get_pressed()
        # left
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 1
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 3
                self.stand_timer += 1
        # right
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 0
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 2
                self.stand_timer += 1
        #up
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.acc.y = -PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 4
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 5
                self.stand_timer += 1
        #down
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.acc.y = PLAYER_ACC
            if self.stand_timer >= 10:
                self.frame = 6
                self.walk_timer += 1
            elif self.walk_timer >= 10:
                self.frame = 7
                self.stand_timer += 1
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_shot > bullet_rate:
                self.last_show = now
                dir = vec(1,0).rotate(-self.rot)
                pos = self.pos + barrel_offset.rotate(-self.rot)
                self.vel = vec(-kickback,0).rotate(-self.rot)
                if keys[pg.K_SPACE] and keys[pg.K_LEFT] or keys[pg.K_SPACE] and keys[pg.K_a]:
                        self.rot = 180
                elif keys[pg.K_SPACE] and keys[pg.K_RIGHT] or keys[pg.K_SPACE] and keys[pg.K_d]:
                        self.rot = 0
                elif keys[pg.K_SPACE] and keys[pg.K_UP] or keys[pg.K_SPACE] and keys[pg.K_w]:
                        self.rot = 90
                elif keys[pg.K_SPACE] and keys[pg.K_DOWN] or keys[pg.K_SPACE] and keys[pg.K_s]:
                        self.rot = 270
##                print(pos,dir)
                Bullet(self.game,pos,dir,self.rot)
                
        # wrap around the sides of the screen   
##        if self.pos.x > WIDTH - 15:
##            self.acc = vec(0,0)
##            self.vel = vec(0,0)
##            self.pos.x -= 0.1
##        if self.pos.x < 15:
##            self.acc = vec(0,0)
##            self.vel = vec(0,0)
##            self.pos.x += 0.1
##        if self.pos.y > HEIGHT - 20:
##            self.acc = vec(0,0)
##            self.vel = vec(0,0)
##            self.pos.y -= 0.1
##        if self.pos.y < 20:
##            self.acc = vec(0,0)
##            self.vel = vec(0,0)
##            self.pos.y += 0.1
        # apply friction
        self.acc += self.vel * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        
      

        self.rect.center = self.pos



class Wall(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites,game.walls
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    
class Floor(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites,game.floors
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.floor_img
        self.rect =self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class Mob(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites,game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.hit_rect = mob_hit_rect.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x,y) * TILESIZE
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.center = self.pos
        self.rot = 0
        
    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1,0))
##        print(self.rot)
        if 45 >= self.rot >= -45:
            self.image = pg.transform.rotate(self.game.mob_img, 0)
        if 135 >= self.rot >= 45:
            self.image = pg.transform.rotate(self.game.mob_img, 90)
        if self.rot >= 135 or self.rot <= -135:
            self.image = pg.transform.rotate(self.game.mob_img, 180)
        if self.rot <= -45 and self.rot >= -135:
            self.image = pg.transform.rotate(self.game.mob_img, -90)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(mob_speed,0).rotate(-self.rot)
        self.acc +=self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt **2
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self,self.game.walls,'y')
        self.rect.center = self.hit_rect.center
    
class Bullet(pg.sprite.Sprite):
    def __init__(self,game,pos,dir,rot):
        self.groups = game.all_sprites, game.bullets
        self.game = game
        pg.sprite.Sprite.__init__(self,self.groups)
        self.dir = dir
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-gun_spread, gun_spread)
        self.vel = dir.rotate(spread) * bullet_speed
        self.spawn_time = pg.time.get_ticks()
        self.rot = rot
    
    def update(self):
        self.pos += self.vel *self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self,self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > bullet_lifetime:
            self.kill()
        if self.rot == 0:
            self.image = pg.transform.rotate(self.game.bullet_img, -90)
        elif self.rot == 90:
            self.image = pg.transform.rotate(self.game.bullet_img, 0)
        elif self.rot == 180:
            self.image = pg.transform.rotate(self.game.bullet_img, 90)
        elif self.rot == 270:
            self.image = pg.transform.rotate(self.game.bullet_img, 180)
##        print(self.rot)