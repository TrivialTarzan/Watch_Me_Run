import pygame

pygame.init()

def menu_screen(welcome_screen, level):
    SCREEN.blit(menu_bg_surface_1, (0,0))
    # SCREEN.blit(torso_surface, torso_rect)
    
    if welcome_screen: 
        SCREEN.blit(game_name,game_name_rect)
        SCREEN.blit(game_message_1,game_message_1_rect)
        SCREEN.blit(game_message_2,game_message_2_rect)
    else:
        if level == 2: 
            SCREEN.blit(score_message,score_message_rect)
            SCREEN.blit(score_message_1,score_message_1_rect)
        if level == 3:
            pass
        if level == 4:
            pass    


WIDTH = 800 
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# fonts
main_font_1 = pygame.font.Font("PyGame\Watch_me_run\\fonts\LIQUIDISMPART2.TTF", 30)
main_font_2 = pygame.font.Font("PyGame\Watch_me_run\\fonts\LIQUIDISMPART2.TTF", 40)
secondary_font_1 = pygame.font.Font("PyGame\Watch_me_run\\fonts\Gypsy Curse.ttf", 50)
secondary_font_2 = pygame.font.Font("PyGame\Watch_me_run\\fonts\Freakshow.ttf", 50)
secondary_font_3 = pygame.font.Font("PyGame\Watch_me_run\\fonts\Them People.ttf", 50)


# menu screen
torso_surface = pygame.image.load('PyGame\Watch_me_run\images\BG_and_else\Torso.png').convert_alpha()
torso_surface = pygame.transform.rotozoom(torso_surface,0,2)  # probably best looking
torso_rect = torso_surface.get_rect(center = (400,190))

game_name = secondary_font_3.render('Watch   Me   Run', False, "Black")
game_name_rect = game_name.get_rect(center = (400,140))


# messages
game_message_1 = main_font_1.render('Just run', False, (255,0,0))
game_message_2 = main_font_1.render('Press space to continue', False, (255,70,0))
game_message_1_rect = game_message_1.get_rect(center=(400,200))
game_message_2_rect = game_message_2.get_rect(center=(400,240))


score_message = main_font_2.render(f'Life hurts a lot more',False,"Black")
score_message_1 = main_font_2.render(f'than death',False,"Black")
score_message_rect = score_message.get_rect(center = (400,170))
score_message_1_rect = score_message_1.get_rect(center = (400,220))

# background
bg_surface_1 = pygame.transform.scale(pygame.image.load("PyGame\Watch_me_run\images\BG_and_else\BG.png"), (WIDTH, HEIGHT)).convert()
menu_bg_surface_1 = pygame.transform.scale(pygame.image.load("PyGame\Watch_me_run\images\BG_and_else\menu_BG.png"), (WIDTH, HEIGHT)).convert()

