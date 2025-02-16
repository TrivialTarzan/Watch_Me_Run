import pygame
import random
import enemies_animation


class Enemies(pygame.sprite.Sprite):
    
    def __init__(self, stage, MAX_UP, MAX_DOWN):
        super().__init__()
        self.MAX_UP = MAX_UP
        self.MAX_DOWN = MAX_DOWN
        self.stage = stage
        self.move_up = bool(random.getrandbits(1))  # Losowy początkowy kierunek góra/dół
        
        self.enemy_index = 0
        self.y = random.randint(MAX_UP, MAX_DOWN)
        self.x = random.randint(900, 1100)
        
        if self.stage == 1:
            self.frames = enemies_animation.demon()
        elif self.stage == 2:
            self.frames = enemies_animation.eye()
        elif self.stage == 3:
            self.frames = enemies_animation.bat()
            
        self.image = self.frames[self.enemy_index]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

        # Losowa prędkość początkowa
        self.speed_x = random.randint(2, 5)
        self.speed_y = random.randint(1, 3)

    def animation(self):
        self.enemy_index += 0.11
        if self.enemy_index >= len(self.frames):
            self.enemy_index = 0
        self.image = self.frames[int(self.enemy_index)]

    def stop_animation_when_leave_screen(self):
        # Kiedy przeciwnicy opuszczają ekran, znikają
        if self.rect.right <= -100 or self.rect.bottom >= 500 or self.rect.top < -100:
            self.kill()

    def movement(self):
        # Poruszanie się w lewo z losową prędkością
        self.rect.x -= self.speed_x

        # Losowy dryf w poziomie (czasem nieznacznie przyspiesza lub zwalnia)
        if random.randint(0, 50) == 0:
            self.speed_x = random.randint(2, 5)

        # Ruch góra/dół z losowymi zmianami kierunku
        if self.move_up:
            self.rect.y -= self.speed_y
        else:
            self.rect.y += self.speed_y

        # Losowa zmiana kierunku co jakiś czas
        if random.randint(0, 60) == 0:  # Co ok. 60 klatek może zmienić kierunek
            self.move_up = not self.move_up

        # Ograniczenia wysokości
        if self.rect.bottom >= 400:
            self.move_up = True
        elif self.rect.top <= 50:
            self.move_up = False

    def update(self):
        self.animation()
        self.movement()
        self.stop_animation_when_leave_screen()
