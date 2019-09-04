import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Реагирует на нажатие клавиш'''
    if event.key == pygame.K_DOWN: 
        ship.moving_down = True
    elif event.key == pygame.K_UP: 
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    '''Создает новую пулю если максимум еще не достигнут'''
    # создание новой пули и включение ее в группу bullets
    if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    '''Реагирует на отпускание клавиш'''
    if event.key == pygame.K_DOWN: 
        ship.moving_down = False
    elif event.key == pygame.K_UP: 
        ship.moving_up = False


def check_events(ai_settings, screen, ship, bullets):
    '''отслеживание событий клавиатуры и мыши'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    '''Обновляет изображения на экране  и отоброжает новый экран'''
    # при каждом проходе цикла прорисовывается экран
    screen.fill(ai_settings.bg_color)

    # все пули выводятся позади изображения корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # отслеживание последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(bullets, ai_settings):
    """Обновите положение пуль и избавьтесь от старых пуль."""
    # Обновить позиции пули.
    bullets.update()

    # Избавьтесь от исчезнувших пуль.
    for bullet in bullets.copy():
        if bullet.rect.right >= ai_settings.screen_width:
            bullets.remove(bullet)
