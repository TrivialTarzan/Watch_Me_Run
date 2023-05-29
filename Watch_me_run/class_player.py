import pygame
import player_animation

class Player(pygame.sprite.Sprite):
    
    def __init__(self, starting_point, velocity, width, height, max_up, max_down, stage):
        super().__init__()
        
        self.STARTING_POINT = starting_point
        self.VELOCITY = velocity
        self.WIDTH = width
        self.HEIGHT = height
        self.MAX_UP = max_up
        self.MAX_DOWN = max_down
        self.stage = stage
        
        self.change_direction = False 
        self.change_index = 0
        self.gravity= 0
        self.jumped = False
        
        self.movement = player_animation.walk()
        self.jump_image = player_animation.jump()
        
        self.image = self.movement[0 if self.change_direction else 1][self.change_index]
        
        if self.stage == 1:
            self.rect = self.image.get_rect(midbottom = (self.STARTING_POINT, self.MAX_DOWN))
        elif self.stage == 2:    
            self.rect = self.image.get_rect(midbottom = (self.STARTING_POINT, self.MAX_DOWN+40))
    
    def stage_update(self, stage):
        self.stage = stage
    
        
    def keys_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and self.rect.bottom >= (self.MAX_DOWN if self.stage == 1 else self.MAX_DOWN+40) and self.stage in [1, 2]:
            self.gravity = -25
            player_animation.jump_sound().play()
            
        if keys[pygame.K_a] and self.rect.left > self.VELOCITY*2:
            self.change_direction = False        
            self.rect.x -= self.VELOCITY
            
        if keys[pygame.K_d] and self.rect.right <= self.WIDTH - self.VELOCITY*2:
            self.change_direction = True
            self.rect.x +=  self.VELOCITY
            
        if keys[pygame.K_w] and self.rect.y - self.VELOCITY >= self.MAX_UP and self.stage not in [1]:
            self.rect.y -= self.VELOCITY
            
        if keys[pygame.K_s] and self.rect.y + self.VELOCITY <= self.MAX_DOWN and self.stage not in [1]:
            self.rect.y += self.VELOCITY  
    
    def adjust_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.stage == 1:
            if self.rect.bottom >= self.MAX_DOWN:
                self.rect.bottom = self.MAX_DOWN
        elif self.stage == 2:
            if self.rect.bottom >= self.MAX_DOWN+40:
                self.rect.bottom = self.MAX_DOWN+40            
         
    def animation(self):
        self.change_index += 0.1
        
        if self.change_index >= len(self.movement):
            self.change_index = 0
        
        if self.rect.bottom < self.MAX_DOWN:
            self.image = self.jump_image[0 if self.change_direction else 1]
        else:    
            self.image = self.movement[0 if self.change_direction else 1][int(self.change_index)]     
              
    def update(self):
        self.keys_input()
        self.adjust_gravity()
        self.animation()                      