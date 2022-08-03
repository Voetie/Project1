import pygame
import random
import time, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player/running/tile000.png")
        self.running_list = ["tile000","tile001","tile002","tile003","tile004","tile005","tile006"]
        self.jumping_list_start = ["tile145","tile146","tile147","tile148"]
        self.jumping_list_end = ["tile149","tile150","tile151","tile153","tile154","tile155"]
        self.attack_list = ["tile224","tile225","tile226"]
        self.running_frame = 0
        self.jumping_frame = 0
        self.attack_frame = 0
        self.animation_timer = 0
        self.rect = self.image.get_rect()
        self.rect.center = (880, 750) 
        self.gravity = 1
        self.vx = 15
        self.vy = 10
        self.x = 848
        self.y = 896
        self.jump = False
        self.attack_bool = False
        self.jump_animation_start = 0
        self.face_left = False
        self.grounded = False
        self.space_cooldown = 0

    def mouseclick(self, events) -> bool:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True

    def keyPressed(self, inputKey):
        if self.keys[inputKey]:
            return False
        else:
            return True

    def movement(self, events):
        self.keys = pygame.key.get_pressed()

        if self.keyPressed(pygame.K_d) or self.keyPressed(pygame.K_q):
            self.image = pygame.image.load("images/player/running/tile000.png")
            if self.face_left:
                self.image = pygame.transform.flip(self.image, True, False)
                
        if self.keys[pygame.K_d]:
            self.rect.move_ip(self.vx, 0)
            tile = self.running_list[self.running_frame%7]
            self.image = pygame.image.load("images/player/running/"+ tile +".png")
            self.running_frame +=1
            self.face_left = False

        if self.keys[pygame.K_q]:
            self.rect.move_ip(-self.vx, 0)
            tile = self.running_list[self.running_frame%7]
            self.image = pygame.image.load("images/player/running/"+ tile +".png")
            self.image = pygame.transform.flip(self.image, True, False)
            self.running_frame +=1
            self.face_left = True
        
        if self.mouseclick(events):
            self.attack_bool = True


        if self.keys[pygame.K_SPACE]:
            if self.jump == False:
                self.jump = True
            if self.grounded:
                self.grounded = False


    def update(self, display):
        if self.jump:
            if self.grounded:
                self.jump = False
                self.vy = 10
                self.jumping_frame = 0
                self.jump_animation_start = 0
            else:
                if self.jump_animation_start == 0:
                    tile = self.jumping_list_start[self.jumping_frame%4]
                    self.image = pygame.image.load("images/player/jump/"+ tile +".png")
                    self.jumping_frame += 1
                    if self.jumping_frame == 4:
                        self.jump_animation_start = 1
                        self.jumping_frame = 0
                else:
                    tile = self.jumping_list_end[self.jumping_frame%3]
                    self.image = pygame.image.load("images/player/jump/"+ tile +".png")
                    self.jumping_frame += 1
                #if self.face_left:
                    #self.image = pygame.transform.flip(self.image, True, False)
                self.rect.move_ip(0, self.vy*-5)
                self.vy -= self.gravity

        if self.attack_bool:
            tile = self.attack_list[self.attack_frame%3]
            self.image = pygame.image.load("images/player/attack/"+ tile +".png")
            self.attack_frame += 1
            pygame.time.delay(15)
            if self.attack_frame == 3:
                self.attack_bool = False
                self.attack_frame = 0

        if self.face_left:
            self.image = pygame.transform.flip(self.image, True, False)

    def floorcollision(self, sprite2):
        self.rect.bottom = sprite2.return_rect().top
        self.grounded = True

    def draw(self, surface): 
        surface.blit(self.image, self.rect)
    
    def attack(self):
        for i in range(9):
            tile = self.attack_list[i]
            self.image = pygame.image.load("images/player/attack/"+ tile +".png")
        self.attack_bool = False
