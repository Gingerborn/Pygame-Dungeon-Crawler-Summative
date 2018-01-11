import pygame as pg
from random import uniform
from map import collide_hit_rect
from settings import *


vec = pg.math.Vector2



def collide_with_walls(sprite, group,dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite,group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width/2
            if sprite.vel.x < 0:
               sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width/2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite,group, False,collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height/2 
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height/2 
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y



class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = player_hit_rect
        self.hit_rect.center = self.rect.center
        self.vel = vec(0,0)
        self.pos = vec(x,y)*tilesize
        self.rot = 0
        self.last_shot = 0
        
    def get_keys(self):
        self.rot_speed = 0
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = player_rot_speed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -player_rot_speed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(player_speed,0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-player_speed / 2,0).rotate(-self.rot)
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_shot > bullet_rate:
                self.last_show = now
                dir = vec(1,0).rotate(-self.rot)
                pos = self.pos + barrel_offset.rotate(-self.rot)
                Bullet(self.game,pos,dir)
                self.vel = vec(-kickback,0).rotate(-self.rot)
            
            
        
    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self,self.game.walls,'y')
        self.rect.center = self.hit_rect.center
   
class Bullet(pg.sprite.Sprite):
    def __init__(self,game,pos,dir):
        self.groups = game.all_sprites, game.bullets
        self.game = game
        pg.sprite.Sprite.__init__(self,self.groups)
        self.image = game.bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        spread = uniform(-gun_spread, gun_spread)
        self.vel = dir.rotate(spread) * bullet_speed
        self.spawn_time = pg.time.get_ticks()
    
    def update(self):
        self.pos += self.vel *self.game.dt
        self.rect.center = self.pos
        if pg.sprite.spritecollideany(self,self.game.walls):
            self.kill()
        if pg.time.get_ticks() - self.spawn_time > bullet_lifetime:
            self.kill()


class Mob(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = mob_hit_rect.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x,y) * tilesize
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.rect.center = self.pos
        self.rot = 0
        
    def update(self):
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1,0))
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)
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

        
        

        
class Wall(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.gamae = game
        self.image = game.wall_img
##        self.image = pg.Surface((tilesize,tilesize))
##        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x *tilesize
        self.rect.y = y * tilesize