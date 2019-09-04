import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''инициализирует корабль и задает его начальную позицию'''
        self.screen = screen
        self.ai_settings = ai_settings

        # загрузка изображения корабля и получения прямоугодьника
        # self.image = pygame.image.load('./figures/crash_course12-01.png')
        # self.image = pygame.transform.scale(self.image, (50, 50))
        # self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # каждый кораболь появляется у нижненго края экрана
        self.rect = pygame.Rect(0, 0, ai_settings.ship_width, ai_settings.ship_height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.color = ai_settings.ship_color

        # сохранение вещественной координаты корабля
        self.center = float(self.rect.centerx)

        # флаги перемещения
        self.moving_right = False
        self.moving_left = False


    def center_ship(self):
        '''размещает корабль в центре нижней стороны'''
        self.center = self.screen_rect.centerx

        
    def update(self):
        '''обновить позицию корабля с учетом флага'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''рисует корабль в текушей позиции'''
        # self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect)