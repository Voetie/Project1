import pygame
import time, sys

class World1Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/world1/ground_objects/world1_cave_floor.png")
        self.rect = self.image.get_rect()
        self.rect.center = (880, 892.5) 
        

    def return_rect(self):
        return self.rect

    def draw(self, surface):
        surface.blit(self.image, self.rect)