import pygame
import random
from pygame.locals import *

pygame.init()

win=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#win=pygame.display.set_mode((500, 500)) 
pygame.display.set_caption('Sophi game')

pygame.event.set_grab(True) # Keeps the cursor within the pygame window

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = False
        else:
            win.fill([random.randint(0,255),random.randint(0,255),random.randint(0,255)])
            pygame.display.update()
