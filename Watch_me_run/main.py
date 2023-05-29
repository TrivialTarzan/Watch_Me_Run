import os
import pygame
from class_player import Player 
from class_enemies import Enemies
import game_functions

# initialize pygame
pygame.init()

# important constants
WIDTH = 800 
HEIGHT = 400
FPS = 25
STARTING_POINT = 60
VELOCITY = 3

# the area where the player and enemies can move/spawn
MAX_UP = 280   
MAX_DOWN = 330

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.display.set_caption("Watch Me Run!")

clock = pygame.time.Clock()
stage = 2

#  the time it takes enemies to respawn 
respawn_time = 4500

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player(STARTING_POINT ,VELOCITY, WIDTH, HEIGHT, MAX_UP, MAX_DOWN, stage))

enemies_group = pygame.sprite.Group()

# setting up the TIMER that creates the enemy creature at a fixed time interval
enemies_timer = pygame.USEREVENT + 1
if stage == 1:
    pygame.time.set_timer(enemies_timer, respawn_time)
elif stage == 2:
    pygame.time.set_timer(enemies_timer, respawn_time)   

            
def collision_check():
    global stage
    
    # pygame.sprite.spritecollide(sprite, group, bool)
    if pygame.sprite.spritecollide(player.sprite, enemies_group, False):
        enemies_group.empty()
        # stage += 1
        return False
    else: 
        return True


def main():
    global stage, respawn_time
    
    active = False
    welcome_screen = True
    start_time = 0
        
    while True:
        
        # event loop checks for all possible inputs
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if active:
                if event.type == enemies_timer:
                    enemies_group.add(Enemies(stage, MAX_UP, MAX_DOWN))
                    
            else:
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    active = True
                    start_time = pygame.time.get_ticks()     
        
        if active:
            welcome_screen = False
              
            game_functions.game_screen(stage)  # draw BG SCREEN
                        
            player.draw(SCREEN)                # draw PLAYER
            player.update()
            
            enemies_group.draw(SCREEN)         # draw ENEMIES
            enemies_group.update()
            
            active = collision_check()
           

        else:
            game_functions.menu_screen(welcome_screen, stage)
        
        
        clock.tick(FPS)    
        pygame.display.update()     

        
if __name__ == "__main__":
    main() 
         