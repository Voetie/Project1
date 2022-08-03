import pygame 
from pygame.locals import *
from pygame import mixer
import time, sys

from current_world import CurrentWorld
from world_1 import World1

pygame.init()
pygame.display.set_caption("Escapegame Team 10")
gameclock = pygame.time.Clock()
keys = pygame.key.get_pressed()


FPS = 144
worldnow = CurrentWorld()
world_1 = World1( worldnow)

while True:
    gameclock.tick(FPS)
    mousex, mousey = pygame.mouse.get_pos()
    pygame.display.update() 
    pygame.time.delay(30)

    #print(mousex, mousey)

    events = pygame.event.get()
    for event in events :
        if event.type == pygame.constants.QUIT:
            pygame.quit()
            sys.exit()

    if worldnow.get_current_world() == 0:
        world_1.worldactions(events, mousex, mousey)
        world_1.act(events)

