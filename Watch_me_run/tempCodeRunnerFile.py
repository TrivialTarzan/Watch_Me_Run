import pygame
import random
import enemies_animation


class Enemies(pygame.sprite.Sprite):
    
    def __init__(self, stage, MAX_UP, MAX_DOWN):
        super().__init__()
        self.MAX_UP = MAX_UP
        self.MAX_DOWN = MAX_DOWN
        self.stage = stage
        self.move_up = True
        
        self.enemy_index = 0
        self.y =  random.randint(MAX_UP, MAX_DOWN)
        self.x = random.randint(900,1100)
        
        if self.stage == 1:
            self.frames = enemies_animation.demon()
            
        elif self.stage ==  2:   
            self.frames = enemies_animation.eye()
            
        elif self.stage == 3:
            self.frames = enemies_animation.bat()
            
        self.image = self.frames[self.enemy_index]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))      
        
    def animation(self):
        self.enemy_index += 0.11
        if self.enemy_index >= len(self.frames):
            self.enemy_index = 0
         
        self.image = self.frames[int(self.enemy_index)]
        
    def stop_animation_when_leave_screen(self):
        # when enemies leave the screen they disappear
        if self.rect.right <= -100 or self.rect.bottom >= 500 or self.rect.top < -100:
            self.kill()
             
                 
    def movement(self):
        # left movement
        self.rect.x -= 3
        
        # up and down movement
        self.rect.y += -2 if self.move_up else 2
        
        if self.rect.bottom >= 400: self.move_up = True
        elif self.rect.top <= 50: self.move_up = False
        
    def update(self):
        self.animation()
        self.movement()
        self.stop_animation_when_leave_screen()          
