#jumpy platform game
import pygame as pg
import random
from settings import *
from sprites import *

pg.init()

class Game:
    def __init__(self,folder):
        #initialize game window
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.folder = folder


    def new(self,folder):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player(folder)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()

    def events(self):
        # game loops - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        #game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        #after drawing everything, flip the display
        pg.display.flip()

def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface,textSurface.get_rect()

def ninja():
    folder = ninja_folder
    g = Game(folder)
    while g.running:
        g.new(folder)
        

def knight():
    folder = knight_folder
    g = Game(folder)
    while g.running:
        g.new(folder)

def wizard():
    folder = wizard_folder
    g = Game(folder)
    while g.running:
        g.new(folder)

def thief():
    folder = thief_folder
    g = Game(folder)
    while g.running:
        g.new(folder)

def quitgame():
    pg.quit()
    quit()

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

def character_select():
    char_intro = True
    while char_intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        gameDisplay.fill(BLACK)
        button("Knight",WIDTH*0.25,HEIGHT*0.05,WIDTH / 2,HEIGHT / 10,WHITE,RED,knight)
        button("Wizard",WIDTH*0.25,HEIGHT*0.25,WIDTH / 2,HEIGHT / 10,WHITE,GREEN,wizard)
        button("Thief",WIDTH*0.25,HEIGHT*0.45,WIDTH / 2,HEIGHT / 10,WHITE,BLUE,thief)
        button("Ninja",WIDTH*0.25,HEIGHT*0.65,WIDTH / 2,HEIGHT / 10, WHITE, YELLOW,ninja)
        button("Quit",WIDTH*0.25,HEIGHT*0.85,WIDTH / 2,HEIGHT / 10,WHITE,RED,quitgame)
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
