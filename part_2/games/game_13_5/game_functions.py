import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship):
    '''Реагирует на нажатие клавиш'''
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = True


def check_keyup_events(event, ship):
    '''Реагирует на отпускание клавиш'''
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = False
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = False


def check_events(ai_settings, screen, ship):
    '''отслеживание событий клавиатуры и мыши'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    '''Обновляет изображения на экране  и отоброжает новый экран'''
    # при каждом проходе цикла прорисовывается экран
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    
    # отслеживание последнего прорисованного экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets):
    """Обновите положение пуль и избавьтесь от старых пуль."""
    if len(bullets) == 0:
        new_bullet = Bullet(ai_settings, screen)
        bullets.add(new_bullet)
    
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom >= ai_settings.screen_height:
            bullets.remove(bullet)
            update_bullets(ai_settings, screen, ship, bullets)
            print('Не поймал')
        elif pygame.sprite.spritecollideany(ship, bullets):
            bullets.remove(bullet)
            update_bullets(ai_settings, screen, ship, bullets)
            print('Поймал')

    # collisions = pygame.sprite.groupcollide(bullets, ship, True, True)


