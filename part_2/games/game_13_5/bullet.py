import pygame
from pygame.sprite import Sprite
from random import randint

class Bullet(Sprite):
    '''Класс для управления пулями, выпущенными кораблем'''

    def __init__(self, ai_settings, screen):
        '''Создает объект пули в текушей позиции корабля'''
        super().__init__()
        self.screen = screen

        # создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = randint(0, ai_settings.screen_width)
        self.rect.top = 0
        
        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # позиции пцули хранится в вещественном формате
        self.y += self.speed_factor
        # обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        '''Вывод пули на экран'''
        pygame.draw.rect(self.screen, self.color, self.rect)
