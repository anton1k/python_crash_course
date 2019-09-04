import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Класс для управления пулями, выпущенными кораблем'''

    def __init__(self, ai_settings, screen, ship):
        '''Создает объект пули в текушей позиции корабля'''
        super(Bullet, self).__init__()
        self.screen = screen

        # создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
        
        # Store a decimal value for the bullet's position.
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # позиции пцули хранится в вещественном формате
        self.x += self.speed_factor
        # обновление позиции прямоугольника
        self.rect.x = self.x

    def draw_bullet(self):
        '''Вывод пули на экран'''
        pygame.draw.rect(self.screen, self.color, self.rect)
