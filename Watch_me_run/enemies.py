import pygame
import random

class Enemies(pygame.sprite.Sprite):
    
    def __init__(self, level, MAX_UP, MAX_DOWN):
        super().__init__()
        self.enemy_index = 0
        self.y =  random.randint(MAX_UP, MAX_DOWN)
        self.x = random.randint(900,1100)
        
        if level == 1:
            ghost_1 = pygame.image.load('PyGame\Watch_me_run\images\Enemies\Ghost\Ghost1.png').convert_alpha()
            ghost_2 = pygame.image.load('PyGame\Watch_me_run\images\Enemies\Ghost\Ghost3.png').convert_alpha()
            self.frames = [ghost_1, ghost_2]
            
        elif level ==  2:   
            eye_1 = pygame.image.load('PyGame\Watch_me_run\images\Enemies\Eye\eye_fire2.png').convert_alpha()
            eye_2 = pygame.image.load('PyGame\Watch_me_run\images\Enemies\Eye\eye_fire3.png').convert_alpha()
            self.frames = [eye_1, eye_2]
            
        elif level == 3:
            bat_1 = pygame.image.load('PyGame\Watch_me_run\images\Enemies\Bat\\bat_1.png').convert_alpha()
            bat_2 = pygame.image.load('PyGame\Watch_me_run\images\Enemies\Bat\\bat_2.png').convert_alpha()
            self.bat_dash = pygame.image.load('PyGame\Watch_me_run\images\Enemies\Bat\\bat_dash.png').convert_alpha()
            self.frames = [bat_1, bat_2]
            
        self.image = self.frames[self.enemy_index]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))      
        
    def animation(self):
        self.enemy_index += 0.09
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
