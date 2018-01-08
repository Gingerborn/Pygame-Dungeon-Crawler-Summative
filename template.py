import pygame
import random
#from settings import *

width = 480
height = 360
fps = 30

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    
    clock.tick(fps)
    
    screen.fill(black)
    pygame.display.flip()