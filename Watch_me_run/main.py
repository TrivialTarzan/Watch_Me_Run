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
FPS = 60
VELOCITY = 3

# the area where the player and enemies can move/spawn
MAX_UP = 280   
MAX_DOWN = 340

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# creating paths relative to my current script location
bg_path_1 = os.path.join(BASE_DIR, "images", "BG_and_else", "BG.png")
bg_path_2 = os.path.join(BASE_DIR, "images", "BG_and_else", "concepts_1.png")
 
pygame.display.set_caption("Watch Me Run!")

clock = pygame.time.Clock()
stage = 1

# background
bg_surface_1 = pygame.transform.scale(pygame.image.load(bg_path_1), (WIDTH, HEIGHT)).convert()
bg_surface_2 = pygame.transform.scale(pygame.image.load(bg_path_2), (WIDTH, HEIGHT)).convert()

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player(VELOCITY, WIDTH, HEIGHT, MAX_UP, MAX_DOWN, stage))

enemies_group = pygame.sprite.Group()

# setting up the TIMER that creates the enemy creature at a fixed time interval
enemies_timer = pygame.USEREVENT + 1
if stage == 1:
    pygame.time.set_timer(enemies_timer, 4000)
elif stage == 2:
    pass    

            
def collision_check():
    # pygame.sprite.spritecollide(sprite, group, bool)
    if pygame.sprite.spritecollide(player.sprite, enemies_group, False):
        enemies_group.empty()
        return False
    else: 
        return True


def main():
    global stage
    
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
            
            # adjust the screen depending on the current level (stage) of the game
            if stage == 1:
                SCREEN.blit(bg_surface_1 , (0,0))
                SCREEN.blit(bg_surface_2, (0,0))
            if stage == 2:
                SCREEN.blit(bg_surface_1 , (0,0))
            
            # game_functions.display_time(start_time)
                        
            player.draw(SCREEN)
            player.update()
            
            enemies_group.draw(SCREEN)
            enemies_group.update()
            
            active = collision_check()

        else:
            game_functions.menu_screen(welcome_screen, stage)
        
        
        clock.tick(FPS)    
        pygame.display.update()     

        
if __name__ == "__main__":
    main() 
         