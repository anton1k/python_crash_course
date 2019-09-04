import sys
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # инициализирует игру, settings и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Создание корабля
    ship = Ship(ai_settings, screen)


    # Создание группы для хранения пуль
    bullets = Group()


    # запуск обычного цикла
    while True:
        gf.check_events(ai_settings, screen, ship)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()
