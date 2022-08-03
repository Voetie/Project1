import pygame
from pygame.locals import *

from world1_obstacles import World1Floor
from player import Player
from current_world import CurrentWorld

class World1:
    def __init__(self, currentworld: CurrentWorld):
        self.DISPLAYSURF = pygame.display.set_mode((1760, 990))
        self.background = pygame.image.load("images/backgrounds/world1_cave.png")
        self.overlay = pygame.image.load("images/backgrounds/overlay.png")
        self.overlay = pygame.transform.scale(self.overlay, (1760,990))
        self.RED = 255,0,0

        self.world1floor = World1Floor()
        self.player = Player()
        self.worldnow = currentworld


    def func_collide(self, sprite1, sprite2) -> bool:
        return sprite1.rect.colliderect(sprite2.rect)


    def act(self, events):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        self.world1floor.draw(self.DISPLAYSURF)
        self.player.movement(events)
        self.player.update(self.DISPLAYSURF)
        self.player.draw(self.DISPLAYSURF)
        self.overlay.blit(self.overlay, (0,0))
        pygame.draw.rect(self.DISPLAYSURF, self.RED, self.world1floor,  2)
        pygame.draw.rect(self.DISPLAYSURF, self.RED, self.player,  2)
        pygame.display.update()

    def worldactions(self, events, mousex, mousey):
        if self.func_collide(self.player, self.world1floor):
            self.player.floorcollision(self.world1floor)