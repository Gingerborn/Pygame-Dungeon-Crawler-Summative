import pygame as pg
import sys
from os import path
import random
from settings import *
from sprites import *
from map import *

class Game:
    def __init__(self):
        self.running = True
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(10,100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'images')
        self.map = Map(path.join(game_folder, 'map2.txt'))
        self.player_img = pg.image.load(path.join(img_folder,player_img)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder,mob_img)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder,wall_img)).convert_alpha()
##        self.player_img = pg.transform.scale(self.player_img,(tilesize,tilesize))
        self.wall_img = pg.transform.scale(self.wall_img,(tilesize,tilesize))
        self.bullet_img = pg.image.load(path.join(img_folder,bullet_img)).convert_alpha()
        self.bullet_img = pg.transform.scale(self.bullet_img,(tilesize,tilesize))

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile =='1':
                    Wall(self,col,row)
                if tile =='p':
                    self.player = Player(self,col,row)
                if tile == 'm':
                    Mob(self,col,row)
        self.camera = Camera(self.map.width,self.map.height)
    
    def run(self):
##Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()
        
    def quit(self):
        pg.quit()
        sys.exit()
    
    def update(self):
        ##Updates portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        ##bullets hitting mobs
        hits = pg.sprite.groupcollide(self.mobs,self.bullets,False,True)
        for hit in hits:
            hit.kill()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
    
    def draw_grid(self):
        for x in range(0, width, tilesize):
            pg.draw.line(self.screen, lightgrey, (x,0),(x,height))
        for y in range(0, height, tilesize):
            pg.draw.line(self.screen, lightgrey, (0,y),(width, y))
    
    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(bgcolor)
##        self.draw_grid()
##        self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
##        pg.draw.rect(self.screen, white, self.player.hit_rect,2) #Use this to check the hitbox
        pg.display.flip()
    
    def show_start_screen(self):
        pass
    
    def show_game_over(self):
        pass
    
    

g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()