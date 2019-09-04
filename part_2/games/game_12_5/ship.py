import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''инициализирует корабль и задает его начальную позицию'''
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображения корабля и получения прямоугодьника
        self.image = pygame.image.load('./figures/crash_course12-01.png')
        self.image = pygame.transform.scale(self.image, (self.ai_settings.size_ship,    self.ai_settings.size_ship))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # каждый кораболь появляется у нижненго края экрана
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # сохранение вещественной координаты корабля
        self.center = float(self.rect.centery)

        # флаги перемещения
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''обновить позицию корабля с учетом флага'''

        if self.moving_up and self.rect.centery > self.ai_settings.size_ship / 2:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.centery < (self.ai_settings.screen_height -    self.ai_settings.size_ship / 2):
            self.center += self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centery = self.center

    def blitme(self):
        '''рисует корабль в текушей позиции'''
        self.screen.blit(self.image, self.rect)