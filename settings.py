import pygame as pg

vec = pg.math.Vector2

##colors
lightgrey = (100,100,100)
darkgrey = (40,40,40)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
brown = (106,55,5)


title = 'My Game'
width = 1024
height = 768
fps = 60
bgcolor = brown

tilesize = 32
gridwidth = width/tilesize
gridheight = height/tilesize
##self.wall_img = pg.transform.scale(self.wall_img, (tilesize, tilesize))
#player
player_speed = 300
player_img = 'gun.png'
player_rot_speed = 250
player_hit_rect = pg.Rect(0,0,35,35)
barrel_offset = vec(30,10)




#GUN STUFF
bullet_img = 'bullet.png'
bullet_speed = 500
bullet_lifetime = 1000
bullet_rate = 150
kickback = 100
gun_spread = 5


##MOBS STUFF
mob_img = "zombie1_hold.png"
mob_speed = 150
mob_hit_rect = pg.Rect(0,0,30,30)

##WALL STUFF
wall_img = 'tile_205.png'


##platform coordinates (x,y,w,h)
##platform_list = [(0,height-40,width,40),
##                 (width/2 -50,height*3/4,100,20),
##                 (300,200,100,20),
##                 (175,100,50,20)]


##
##
##        This is how you add platforms without the platform list
##
##        p1 = Platform(0,height-40,width,40)
##        self.all_sprites.add(p1)
##        self.platforms.add(p1)
##        p2 = Platform(width/2 -50,height*3/4,100,20)
##        self.all_sprites.add(p2)
##        self.platforms.add(p2)


