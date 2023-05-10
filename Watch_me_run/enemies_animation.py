import os
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def demon():
    demon_path_1 = os.path.join(BASE_DIR, "images", "Enemies", "Demon", "demon_1.png")
    demon_path_2 = os.path.join(BASE_DIR, "images", "Enemies", "Demon", "demon_2.png")
    demon_path_3 = os.path.join(BASE_DIR, "images", "Enemies", "Demon", "demon_3.png")
    demon_path_4 = os.path.join(BASE_DIR, "images", "Enemies", "Demon", "demon_4.png")
    
    demon_1 = pygame.image.load(demon_path_1).convert_alpha()
    demon_2 = pygame.image.load(demon_path_2).convert_alpha()
    demon_3 = pygame.image.load(demon_path_3).convert_alpha()
    demon_4 = pygame.image.load(demon_path_4).convert_alpha()
    
    return [demon_1, demon_2, demon_3, demon_4]


def eye():
    eye_path_1 = os.path.join(BASE_DIR, "images", "Enemies", "Eye", "eye_fire2.png")
    eye_path_2 = os.path.join(BASE_DIR, "images", "Enemies", "Eye", "eye_fire3.png")
    
    eye_1 = pygame.image.load(eye_path_1).convert_alpha()
    eye_2 = pygame.image.load(eye_path_2).convert_alpha()
    
    return [eye_1, eye_2]


def bat():
    bat_path_1 = os.path.join(BASE_DIR, "images", "Enemies", "Bat", "bat_1.png")
    bat_path_2 = os.path.join(BASE_DIR, "images", "Enemies", "Bat", "bat_2.png")
    bat_path_3 = os.path.join(BASE_DIR, "images", "Enemies", "Bat", "bat_dash.png")
    
    bat_1 = pygame.image.load(bat_path_1).convert_alpha()
    bat_2 = pygame.image.load(bat_path_2).convert_alpha()    
    
    return [bat_1, bat_2]