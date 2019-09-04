import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''инициализирует корабль и задает его начальную позицию'''
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображения корабля и получения прямоугодьника
        self.image = pygame.image.load('./figures/crash_course12-01.png')
        self.image = pygame.transform.scale(self.image, (self.ai_settings.size_ship, self.ai_settings.size_ship))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # каждый кораболь появляется у нижненго края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # сохранение вещественной координаты корабля
        self.center = float(self.rect.centerx)
        self.bott = float(self.rect.bottom)

        # флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''обновить позицию корабля с учетом флага'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.bottom > self.ai_settings.size_ship:
            self.bott -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bott += self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.bott

    def blitme(self):
        '''рисует корабль в текушей позиции'''
        self.screen.blit(self.image, self.rect)