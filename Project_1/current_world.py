import pygame
import time, sys

class CurrentWorld(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.current_world = 0
        
    def get_current_world(self):
        return self.current_world

    def change_world(self, world):
        self.current_world = world