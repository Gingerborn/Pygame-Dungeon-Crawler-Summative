#jumpy platform game
import pygame as pg
import random
from settings import *
from sprites import *
from map import *
import sys 

pg.init()

class Game:
    def __init__(self,folder):
        #initialize game window
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(10,100)
        self.running = True
        self.folder = folder
        self.load_data()
    
    def bullets(self, img):
        self.bullet_img = pg.image.load(os.path.join(bullet_folder,img)).convert_alpha()
        self.bullet_img = pg.transform.scale(self.bullet_img,(TILESIZE,TILESIZE))
        self.bullet_img.set_colorkey(WHITE)

    def load_data(self):
        self.map = Map(map_file)
        self.wall_img = pg.image.load(wall_image_png).convert_alpha()
##        self.bullet_img = pg.image.load(bullet_image_png).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img,(TILESIZE,TILESIZE))
##        self.bullet_img = pg.transform.scale(self.bullet_img,(TILESIZE,TILESIZE))
        self.mob_img = pg.image.load(mob_image_png).convert_alpha()
        self.mob_img = pg.transform.scale(self.mob_img,(TILESIZE,TILESIZE))
        self.player_img2 = pg.image.load(os.path.join(other_folder,player_img3)).convert_alpha()
        self.floor_img = pg.image.load(floor_image_png).convert_alpha()
        self.floor_img = pg.transform.scale(self.floor_img,(TILESIZE,TILESIZE))

    def new(self,folder):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        for row,tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'p':
                    self.player = Player(self.folder,self,col,row)
                if tile == 'm':
                    Mob(self,col,row)
##                    Floor(self,col,row)
##                if tile == '.':
##                    Floor(self,col,row)
                    
        self.camera = Camera(self.map.width,self.map.height)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 100
##            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.groupcollide(self.mobs,self.bullets,False,True)
        for hit in hits:
            hit.kill()
##        pg.display.flip()

    def events(self):
        # game loops - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #game loop - draw
        self.screen.fill(BLACK)
##        self.all_sprites.draw(self.screen)
        #after drawing everything, flip the display
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,self.camera.apply(sprite))
##      This checks hitbox
##        pg.draw.rect(self.screen,WHITE,self.player.hit_rect,2)
        pg.display.flip()
            

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface,textSurface.get_rect()
        
def ninja():
    folder = ninja_folder
    g = Game(folder)
    while g.running:
        g.bullets('shuriken.png')
        g.new(folder)
        
def knight():
    folder = knight_folder
    g = Game(folder)
    while g.running:
        g.bullets('slash.png')
        g.new(folder)

def barbarian():
    folder = barb_folder
    g = Game(folder)
    while g.running:
        g.bullets('slash.png')
        g.new(folder)

def wizard():
    folder = wizard_folder
    g = Game(folder)
    while g.running:
        g.bullets('fireball.png')
        g.new(folder)

def warlock():
    folder = warlock_folder
    g = Game(folder)
    while g.running:
        g.bullets('zombie1_hold.png')
        g.new(folder)
    

def thief():
    folder = thief_folder
    g = Game(folder)
    while g.running:
        g.bullets('shuriken.png')
        g.new(folder)

def secret_tank():
    folder = secret_folder
    g = Game(folder)
    while g.running:
        g.bullets('missile.png')
        g.new(folder)

def quitgame():
    pg.quit()
    quit()
    
def unpause():
    global pause
    pg.mixer.music.unpause()
    pause = False

def paused():
    global pause
    pause = True
    pg.mixer.music.pause()
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(BLACK)
        largeText = pg.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects('Paused',largeText,WHITE)
        TextRect.center = ((WIDTH/2,HEIGHT/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Continue!",WIDTH*0.15,WIDTH*0.75,100,50,GREEN,BRIGHT_GREEN,unpause)
##        button("Character Select",WIDTH*0.45,WIDTH*0.75,200,50,BLUE,BRIGHT_BLUE,go_back)
        button("Quit",WIDTH*0.8,WIDTH*0.75,100,50,RED,BRIGHT_RED,quitgame)
        pg.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pg.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pg.font.Font('freesansbold.ttf',20)
    textSurf,textRect = text_objects(msg,smallText,BLACK)
    textRect.center = ((x+(w/2),(y+(h/2))))
    gameDisplay.blit(textSurf,textRect)

def tank_subclasses():
    tank_intro = True
    while tank_intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(BLACK)
        button("Knight",WIDTH*0.25,HEIGHT*0.1,WIDTH / 2,HEIGHT / 10,WHITE,GREEN,knight)
        button("Barbarian",WIDTH*0.25,HEIGHT*0.45,WIDTH / 2,HEIGHT / 10,WHITE,YELLOW,barbarian)
        button("Quit",WIDTH*0.25,HEIGHT*0.8,WIDTH / 2,HEIGHT / 10,WHITE,BRIGHT_RED,quitgame)
        pg.display.update()
        clock.tick(15)

def hunter_subclasses():
    hunter_intro = True
    while hunter_intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(BLACK)
        button("Thief",WIDTH*0.25,HEIGHT*0.1,WIDTH / 2,HEIGHT / 10,WHITE,RED,thief)
        button("Ninja",WIDTH*0.25,HEIGHT*0.45,WIDTH / 2,HEIGHT / 10,WHITE,MAGENTA,ninja)
        button("Quit",WIDTH*0.25,HEIGHT*0.8,WIDTH / 2,HEIGHT / 10,WHITE,BRIGHT_RED,quitgame)
        pg.display.update()
        clock.tick(15)

def mage_subclasses():
    mage_intro = True
    while mage_intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(BLACK)
        button("Wizard",WIDTH*0.25,HEIGHT*0.3,WIDTH / 2,HEIGHT / 10,WHITE,BLUE,wizard)
        button("Warlock",WIDTH*0.25,HEIGHT*0.6,WIDTH / 2,HEIGHT / 10,WHITE,CYAN,warlock)
        button("Quit",WIDTH*0.25,HEIGHT*0.8,WIDTH / 2,HEIGHT / 10,WHITE,BRIGHT_RED,quitgame)
        pg.display.update()
        clock.tick(15)

def character_select():
    char_intro = True
    while char_intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(BLACK)
        button("Tank",WIDTH*0.25,HEIGHT*0.25,WIDTH / 2,HEIGHT / 10,WHITE,RED,tank_subclasses)
        button("Mage",WIDTH*0.25,HEIGHT*0.45,WIDTH / 2,HEIGHT / 10,WHITE,GREEN,mage_subclasses)
        button("Hunter",WIDTH*0.25,HEIGHT*0.65,WIDTH / 2,HEIGHT / 10,WHITE,BLUE,hunter_subclasses)
        button("Secret",0,HEIGHT - 50,100,50,BLACK,WHITE,secret_tank)
        button("Quit",WIDTH*0.25,HEIGHT*0.85,WIDTH / 2,HEIGHT / 10,WHITE,BRIGHT_RED,quitgame)
        pg.display.update()
        clock.tick(15)

def game_intro():
    gam_intro = True
    while gam_intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(BLACK)
        largeText = pg.font.Font('freesansbold.ttf',250)
        TextSurf, TextRect = text_objects('POWER',largeText,WHITE)
        TextRect.center = ((WIDTH/2,HEIGHT/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Play",WIDTH*0.2,HEIGHT*0.75,100,50,GREEN,BRIGHT_GREEN,character_select)
        button("Quit",WIDTH*0.75,HEIGHT*0.75,100,50,RED,BRIGHT_RED,quitgame)
        
        pg.display.update()
        clock.tick(15)

game_intro()
pg.quit()
