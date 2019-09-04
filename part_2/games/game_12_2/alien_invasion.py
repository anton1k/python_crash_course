import sys
import pygame

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

    # назначение цвета фона
    bg_color = (230, 230, 230)
    
    # запуск обычного цикла
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
