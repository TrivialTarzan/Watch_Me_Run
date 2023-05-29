import os
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def walk():
    walk_right_path_1 = os.path.join(BASE_DIR, "images", "character", "walk_1_right.png")
    walk_right_path_2 = os.path.join(BASE_DIR, "images", "character", "walk_2_right.png")
    
    walk_left_path_1 = os.path.join(BASE_DIR, "images", "character", "walk_1_left.png")
    walk_left_path_2 = os.path.join(BASE_DIR, "images", "character", "walk_2_left.png")
    
    walk_right_1 = pygame.image.load(walk_right_path_1).convert_alpha()
    walk_right_2 = pygame.image.load(walk_right_path_2).convert_alpha()
    walk_left_1 = pygame.image.load(walk_left_path_1).convert_alpha()
    walk_left_2 = pygame.image.load(walk_left_path_2).convert_alpha()
    
    movement_right = [walk_right_1, walk_right_2]
    movement_left = [walk_left_1, walk_left_2]
    
    return [movement_right, movement_left]


def jump():
    jump_right_path = os.path.join(BASE_DIR, "images", "character", "jump_right.png")
    jump_left_path = os.path.join(BASE_DIR, "images", "character", "jump_left.png")
    
    jump_right = pygame.image.load(jump_right_path).convert_alpha()
    jump_left = pygame.image.load(jump_left_path).convert_alpha()   
    
    return [jump_right, jump_left]


def jump_sound():
    jump_sound_path = os.path.join(BASE_DIR, "sounds", "jump.wav")
    
    jump_sound = pygame.mixer.Sound(jump_sound_path)
    jump_sound.set_volume(0.1)
    
    return jump_sound