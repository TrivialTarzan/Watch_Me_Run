import os
import pygame

pygame.init()

def game_screen(stage):
    global change_screen_index
    
    if change_screen_index >= 9:
        change_screen_index = 0
    
    # screen animation
    if check_if_space_pressed() and pygame.K_UP:
        change_screen_index += 1
    
    if stage == 1:
        SCREEN.blit(bg_surface_1, (0,0))
    if stage == 2:
        # change_screen_index += 0.01
        SCREEN.blit(bg_surfaces_2[int(change_screen_index)], (0,0))
    if stage == 3:
        pass  

def menu_screen(welcome_screen, stage):
    SCREEN.blit(menu_bg_surface_1, (0,0))
    # SCREEN.blit(torso_surface, torso_rect)
    
    if welcome_screen: 
        SCREEN.blit(GAME_NAME, game_name_rect)
        SCREEN.blit(game_message_1, game_message_1_rect)
        SCREEN.blit(game_message_2, game_message_2_rect)
    else:
        if stage == 1: 
            SCREEN.blit(score_message,score_message_rect)
            SCREEN.blit(score_message_1,score_message_1_rect)
        if stage == 2:
            pass
        if stage == 3:
            pass    


def display_time(start_time):
    current_time = pygame.time.get_ticks() - start_time
    score_surf = main_font_1.render(f'Timer: {round(current_time/1000, 1)}', False, BLACK)   
    score_rect = score_surf.get_rect(center = (400, 50))
    SCREEN.blit(score_surf, score_rect)
    
    return current_time

def check_if_space_pressed():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        return True
    else: 
        return False
    
def bg_music():
    bg_music_path = os.path.join(BASE_DIR, "sounds", "BG_David_Renda.mp3")
    
    bg_music = pygame.mixer.Sound(bg_music_path)
    bg_music.set_volume(0.2)
    
    return bg_music

change_screen_index = 0 

WIDTH = 800 
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)

# DIR to all the files 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# fonts
FONT_PATH_1 = os.path.join(BASE_DIR, "fonts", "LIQUIDISMPART2.TTF")
FONT_PATH_2 = os.path.join(BASE_DIR, "fonts", "Gypsy Curse.ttf")
FONT_PATH_3 = os.path.join(BASE_DIR, "fonts", "Freakshow.ttf")
FONT_PATH_4 = os.path.join(BASE_DIR, "fonts", "Them People.ttf")

main_font_1 = pygame.font.Font(FONT_PATH_1, 30)
main_font_2 = pygame.font.Font(FONT_PATH_1, 40)
secondary_font_1 = pygame.font.Font(FONT_PATH_2, 50)
secondary_font_2 = pygame.font.Font(FONT_PATH_3, 50)
secondary_font_3 = pygame.font.Font(FONT_PATH_4, 50)

#
TORSO_PATH = os.path.join(BASE_DIR, "images", "BG_and_else", "Torso.png")

torso_surface = pygame.image.load(TORSO_PATH).convert_alpha()
torso_surface = pygame.transform.rotozoom(torso_surface,0,2)  # probably best looking
torso_rect = torso_surface.get_rect(center = (400,190))

#
GAME_NAME = secondary_font_3.render('Watch   Me   Run', False, "Black")
game_name_rect = GAME_NAME.get_rect(center = (400,140))


# messages

game_message_1 = main_font_1.render('Just run', False, (255,0,0))
game_message_2 = main_font_1.render('Press space to continue', False, (255,70,0))
game_message_1_rect = game_message_1.get_rect(center=(400,200))
game_message_2_rect = game_message_2.get_rect(center=(400,240))


score_message = main_font_2.render(f'Life hurts a lot more',False,"Black")
score_message_1 = main_font_2.render(f'than death',False,"Black")
score_message_rect = score_message.get_rect(center = (400,170))
score_message_1_rect = score_message_1.get_rect(center = (400,220))

### BACKGROUNDS ###

# menu
BG_MENU_PATH = os.path.join(BASE_DIR, "images", "BG_and_else", "menu_BG.png")
menu_bg_surface_1 = pygame.transform.scale(pygame.image.load(BG_MENU_PATH ), (WIDTH, HEIGHT)).convert()


# stage 1
BG_PATH_1 = os.path.join(BASE_DIR, "images", "BG_and_else", "concepts_1.png")
bg_surface_1 = pygame.transform.scale(pygame.image.load(BG_PATH_1), (WIDTH, HEIGHT)).convert()

# stage 2
BG_PATHS_2 = [os.path.join(BASE_DIR, "images", "BG_and_else", "BG_stage_2", f"BG_{i}.png") for i in range(1, 11)]
bg_surfaces_2 = [pygame.transform.scale(pygame.image.load(path), (WIDTH, HEIGHT)).convert() for path in BG_PATHS_2]
