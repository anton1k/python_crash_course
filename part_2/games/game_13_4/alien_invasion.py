import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings

def run_game():
    # инициализирует игру, settings и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Создание группы пришельцев
    aliens = Group()

    # Создание флота пришельцев
    gf.creat_fleet(ai_settings, screen, aliens)

    # запуск обычного цикла
    while True:
        gf.check_events(ai_settings, screen)
        gf.update_aliens(ai_settings, screen, aliens)
        gf.update_screen(ai_settings, screen, aliens)

run_game()
