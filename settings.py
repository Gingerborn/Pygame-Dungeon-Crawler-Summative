import pygame as pg
import os

#game options/settings
# define game colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BRIGHT_RED = (255,0,0)
RED = (200,0,0)
BRIGHT_GREEN = (0,255,0)
GREEN = (0,200,0)
BRIGHT_BLUE = (0,0,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)

TITLE = 'Movement'
#changing width and height to anything under 1309 then exitting game with red x
#makes the next run non-playable ('play' button exits game)
# QUESTION WHYTE ABOUT IT #
WIDTH = 1024
HEIGHT = 768
FPS = 60

TILESIZE = 32

player_hit_rect = pg.Rect(0,0,30,30)
player_img3 = 'gun.png'

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,'IMG')
knight_folder = os.path.join(img_folder,'KNIGHT')
wizard_folder = os.path.join(img_folder,'WIZARD')
warlock_folder = os.path.join(img_folder,'WARLOCK')
thief_folder = os.path.join(img_folder,'THIEF')
ninja_folder = os.path.join(img_folder,'NINJA')
barb_folder = os.path.join(img_folder,'BARBARIAN')
secret_folder = os.path.join(img_folder,'TANK')
sound_folder = os.path.join(game_folder,'SOUND')
music_POWER = os.path.join(sound_folder,'Power.wav')
map_file = os.path.join(game_folder, 'map2.txt')
folder = knight_folder
other_folder = os.path.join(img_folder,'OTHERS')

wall_image_png = os.path.join(other_folder,'tile_205.png')
bullet_image_png = os.path.join(other_folder,'bullet.png')

gameDisplay = pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()


