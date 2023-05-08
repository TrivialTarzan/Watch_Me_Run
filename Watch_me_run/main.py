import pygame
from player import Player 
from enemies import Enemies
from menu import menu_screen

# to initialize pygame
pygame.init()

WIDTH = 800 
HEIGHT = 400
FPS = 60
VELOCITY = 3

# the area where the player and enemies can move/spawn
MAX_UP = 250   
MAX_DOWN = 370
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
 
pygame.display.set_caption("Watch Me Run!")

stage = 2
clock = pygame.time.Clock()
main_font = pygame.font.Font("PyGame\Watch_me_run\\fonts\LIQUIDISMPART2.TTF", 40)


# BG
bg_surface_1 = pygame.transform.scale(pygame.image.load("PyGame\Watch_me_run\images\BG_and_else\BG.png"), (WIDTH, HEIGHT)).convert()
bg_surface_2 = pygame.transform.scale(pygame.image.load("PyGame\Watch_me_run\images\BG_and_else\concepts_1.png"), (WIDTH, HEIGHT)).convert()

# collision
collision = pygame.Rect(0, 380, 1000, 20)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player(VELOCITY, WIDTH, HEIGHT, MAX_UP, stage))

enemies_group = pygame.sprite.Group()

### TIMER ###
# setting up the TIMER that creates the enemy creature at a fixed time interval
enemies_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemies_timer, 1500)


def collision_check():
    # pygame.sprite.spritecollide(sprite, group, bool)
    if pygame.sprite.spritecollide(player.sprite, enemies_group,False):
        enemies_group.empty()
        return False
    else: 
        return True


def display_time(start_time):
    current_time = pygame.time.get_ticks() - start_time
    score_surf = main_font.render(f'Timer: {round(current_time/1000, 1)}', False, "Black")   # (64,64,64)
    score_rect = score_surf.get_rect(center = (400, 50))
    SCREEN.blit(score_surf, score_rect)
    # pygame.draw.rect(SCREEN, (145,6,122), score_rect, 3)
    
    return current_time


def main():
    global stage
    
    active = False
    welcome_screen = True
    start_time = 0
    stage = 2
    
        
    while True:
        
        # event loop checks for all possible inputs
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if active:
                if event.type == enemies_timer:
                    enemies_group.add(Enemies(1, MAX_UP, MAX_DOWN))
                    
            else:
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    active = True
                    start_time = pygame.time.get_ticks()     
        
        if active:
            welcome_screen = False
            # level 1 screen
            if stage == 1:
                SCREEN.blit(bg_surface_1 , (0,0))
                display_time(start_time)
            if stage == 2:
                SCREEN.blit(bg_surface_1 , (0,0))
                SCREEN.blit(bg_surface_2, (0,0))
                display_time(start_time)
                        
            player.draw(SCREEN)
            player.update()
            
           # enemies_group.draw(SCREEN)
           # enemies_group.update()
            pygame.display.update() 
            active = collision_check()

        else:
            menu_screen(welcome_screen, stage)
        
        clock.tick(FPS)    
        pygame.display.update()     

        
if __name__ == "__main__":
    main() 
         