import pygame
import random
from player import Player 
from enemies import Enemies

def collision_check():
    # pygame.sprite.spritecollide(sprite, group, bool)
    if pygame.sprite.spritecollide(player.sprite, enemies_group,False):
        enemies_group.empty()
        return False
    else: 
        return True

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = main_font.render(f'Score: {round(current_time/1000, 1)}', False, (255,140,0))   # (64,64,64)
    score_rect = score_surf.get_rect(center = (400, 50))
    SCREEN.blit(score_surf, score_rect)
    # pygame.draw.rect(SCREEN, (145,6,122), score_rect, 3)
    
    return current_time

def menu_screen(welcome_screen):
    SCREEN.fill((0,0,0))
    SCREEN.blit(torso_surface, torso_rect)
    
    score_message = secondary_font_1.render(f'You Survived',False,(111,196,169))
    score_message_rect = score_message.get_rect(center = (400,330))
    SCREEN.blit(game_name,game_name_rect)
    
    if welcome_screen: 
        SCREEN.blit(game_message_1,game_message_1_rect)
        SCREEN.blit(game_message_2,game_message_2_rect)
    else: 
        SCREEN.blit(score_message,score_message_rect)


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

clock = pygame.time.Clock()
main_font = pygame.font.Font("PyGame\Watch_me_run\\fonts\LIQUIDISMPART2.TTF", 50)
secondary_font_1 = pygame.font.Font("PyGame\Watch_me_run\\fonts\Gypsy Curse.ttf", 50)
secondary_font_2 = pygame.font.Font("PyGame\Watch_me_run\\fonts\Freakshow.ttf", 50)
active = False
start_time = 0

# menu screen
torso_surface = pygame.image.load('PyGame\Watch_me_run\images\BG_and_else\Torso.png').convert_alpha()
torso_surface = pygame.transform.rotozoom(torso_surface,0,2)  # probably best looking
torso_rect = torso_surface.get_rect(center = (400,190))

game_name = secondary_font_2.render('Watch   Me   Run!', False, (255,0,0))
game_name_rect = game_name.get_rect(center = (400,40))

game_message_1 = secondary_font_1.render('Survive 30 Seconds', False, (255,0,0))
game_message_2 = secondary_font_1.render('Press space to continue', False, (255,70,0))
game_message_1_rect = game_message_1.get_rect(center=(400,320))
game_message_2_rect = game_message_2.get_rect(center=(400,370))

welcome_screen = True

# background and collinions
bg_surface = pygame.transform.scale(pygame.image.load("PyGame\Watch_me_run\images\BG_and_else\BG.png"), (WIDTH, HEIGHT)).convert()
collision = pygame.Rect(0, 380, 1000, 20)


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player(VELOCITY, WIDTH, HEIGHT, MAX_UP))

enemies_group = pygame.sprite.Group()

### TIMER ###
# setting up the TIMER that creates the enemy creature at a fixed time interval
enemies_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemies_timer, 1500)

while True:
    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    
    # event loop checking for all possible inputs
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if active:
            if event.type == enemies_timer:
                enemies_group.add(Enemies(1, MAX_UP, MAX_DOWN))
                
        else:
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if keys[pygame.K_SPACE]:
                active = True
                start_time = int(pygame.time.get_ticks() / 1000)       
    
    if active:
        welcome_screen = False
        pygame.draw.rect(SCREEN, "blue", collision)
        SCREEN.blit(bg_surface , (0,0))
        display_score()
        
        player.draw(SCREEN)
        player.update()
        
        enemies_group.draw(SCREEN)
        enemies_group.update()
        
        active = collision_check()
    
    else:
        menu_screen(welcome_screen)
    
    clock.tick(FPS)    
    pygame.display.update()     
        
      


  
      # # collision
        # if self.rect.colliderect(collision_1_rect):
        #     self.rect.y -= self.gravity
        #     #    # self.rect.y = collision_1_rect.top - self.rect.top 
        #     # if self.gravity >= 0:
        #     #    # self.rect.y = collision_1_rect.top - self.rect.bottom    
              

# if self.keys[pygame.K_SPACE]:
#             if not self.jumped:
#                 self.gravity = -15
#                 self.jumped = True
#             else:
#                 self.jumped = False   

# collision_1 = pygame.image.load("PyGame\Watch_me_run\images\collisions\\7 — kopia.png").convert()
# collision_1_rect = collision_1.get_rect(midbottom = (50, 370))
# collision_2 = pygame.image.load("PyGame\Watch_me_run\images\collisions\\7.png").convert()
# collision_2_rect = collision_1.get_rect(midbottom = (800, 300))
        
        
    # def add_gravity(self):
    #     if not self.rect.colliderect(collision):
    #         self.gravity += 1
            
    #     # self.gravity += 1
    #     # if self.gravity > 10:
    #     #     self.gravity = 10
    #     self.rect.y += self.gravity
                          