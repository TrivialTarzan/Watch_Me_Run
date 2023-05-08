import pygame
import random 


class Player(pygame.sprite.Sprite):
    
    def __init__(self, velocity, width, height, max_up, stage):
        super().__init__()
        
        self.VELOCITY = velocity
        self.WIDTH = width
        self.HEIGHT = height
        self.MAX_UP = max_up
        self.stage = stage
        
        self.change_direction = False 
        self.change_index = 0
        self.gravity= 0
        self.jumped = False
        
        char_walk_right_1 = pygame.image.load('PyGame\Watch_me_run\images\character\walk_1_right.png').convert_alpha()
        char_walk_right_2 = pygame.image.load('PyGame\Watch_me_run\images\character\walk_2_right.png').convert_alpha()
        char_walk_left_1 = pygame.image.load('PyGame\Watch_me_run\images\character\walk_1_left.png').convert_alpha()
        char_walk_left_2 = pygame.image.load('PyGame\Watch_me_run\images\character\walk_2_left.png').convert_alpha()
        
        # jump_right = pygame.image.load('PyGame\Watch_me_run\images\character\jump_right.png').convert_alpha()
        # jump_left = pygame.image.load('PyGame\Watch_me_run\images\character\jump_left.png').convert_alpha()
        # jump_list = [jump_right, jump_left]
        
        char_movement_right = [char_walk_right_1, char_walk_right_2]
        char_movement_left = [char_walk_left_1, char_walk_left_2]
        self.movement = [char_movement_right, char_movement_left]
        self.image = self.movement[0 if self.change_direction else 1][self.change_index]
        self.rect = self.image.get_rect(midbottom = (60, 330))
        
        self.jump_sound = pygame.mixer.Sound("PyGame\\another game\sounds\jump.mp3")
        self.jump_sound.set_volume(0.2)
        
    def keys_input(self):
        self.keys = pygame.key.get_pressed()
    
        if self.keys[pygame.K_a] and self.rect.left > self.VELOCITY*2:
            self.change_direction = False        
            self.rect.x -= self.VELOCITY
        if self.keys[pygame.K_d] and self.rect.right <= self.WIDTH - self.VELOCITY*2:
            self.change_direction = True
            self.rect.x +=  self.VELOCITY
        if self.keys[pygame.K_w] and self.rect.y - self.VELOCITY >= self.MAX_UP:
            self.rect.y -= self.VELOCITY
        if self.keys[pygame.K_s] and self.rect.bottom <= self.HEIGHT - self.VELOCITY*2:
            self.rect.y += self.VELOCITY 
         
    def animation(self):
        self.change_index += 0.1
        
        if self.change_index >= len(self.movement):
            self.change_index = 0
         
        self.image = self.movement[0 if self.change_direction else 1][int(self.change_index)]     
              
    def update(self):
        self.keys_input()
        self.animation()            
                   