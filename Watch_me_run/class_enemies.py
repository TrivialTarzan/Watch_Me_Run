import pygame
import random
import enemies_animation


class Enemies(pygame.sprite.Sprite):
    
    def __init__(self, stage, MAX_UP, MAX_DOWN):
        super().__init__()
        self.enemy_index = 0
        self.y =  random.randint(MAX_UP, MAX_DOWN)
        self.x = random.randint(900,1100)
        self.stage = stage
        
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
        # when enemies leave the screen they need to disappear
        if self.rect.right <= -100:
            self.kill()      
        
    def update(self):
        self.animation()
        self.rect.x -= 3
        self.stop_animation_when_leave_screen()          
