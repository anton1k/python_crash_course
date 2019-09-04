import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''класс представляющий одного пришельца'''

    def __init__(self, ai_settings, screen):
        '''Инициализирует пришельца и задает его начальную позицию'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('figures/crash_course13-01.png')
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect()

        # каждыйновый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной позиции пришельца
        self.x = float(self.rect.x)

        
    def blitme(self):
        '''ввыводит пришельца в текушем положении'''
        self.screen.blit(self.image, self.rect)