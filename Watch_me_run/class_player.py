import pygame
import player_animation

class Player(pygame.sprite.Sprite):
    
    def __init__(self, velocity, width, height, max_up, max_down, stage):
        super().__init__()
        
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
        self.rect = self.image.get_rect(midbottom = (60, 330))
        
        # self.jump_sound = pygame.mixer.Sound("PyGame\\another game\sounds\jump.mp3")
        # self.jump_sound.set_volume(0.2)
    
    def stage_update(self, stage):
        self.stage = stage
    
        
    def keys_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and self.rect.bottom >= 320 and self.stage in [1]:
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
        if self.rect.bottom >= 330:
            self.rect.bottom = 330
         
    def animation(self):
        self.change_index += 0.1
        
        if self.change_index >= len(self.movement):
            self.change_index = 0
        
        if self.rect.bottom < 330:
            self.image = self.jump_image[0 if self.change_direction else 1]
        else:    
            self.image = self.movement[0 if self.change_direction else 1][int(self.change_index)]     
              
    def update(self):
        self.keys_input()
        self.adjust_gravity()
        self.animation()                      