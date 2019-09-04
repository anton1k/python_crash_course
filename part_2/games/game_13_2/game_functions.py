import sys
import pygame
from alien import Alien
from random import randint

def check_events(ai_settings, screen):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, alien):
    '''Обновляет изображения на экране  и отоброжает новый экран'''
    # при каждом проходе цикла прорисовывается экран
    screen.fill(ai_settings.bg_color)
    alien.draw(screen)
    # отслеживание последнего прорисованного экрана
    pygame.display.flip()


def get_number_aliens_x(ai_settings, alien_width):
    '''Вычисляет колтчесвто пришельцев в ряду'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, alien_height):
    '''Определяет количество рядов, помещающихся на экране'''
    available_space_y = (ai_settings.screen_height - alien_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''Создает пришельца в ряду''' 
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x + randint(-12,12)
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number) + randint(-12,12)
    aliens.add(alien)


def creat_fleet(ai_settings, screen, aliens):
    '''Создает флот пришельцев'''
    # создание пришельца и вычисление количества пришельцев
    # интервал между соседними пришельцами равен одной ширине пришельца

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_row = get_number_rows(ai_settings, alien.rect.height)

    # создание флота пришельцев
    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)
