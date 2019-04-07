#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

import sys
import pygame
from alien import Alien
from random import randint



def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, aliens, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 绘制飞船
    ship.blitme()

    # 在屏幕上绘制编组中的每个外星人
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def create_alien(ai_settings, screen, aliens):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    alien.x = randint(alien_width, available_space_x)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height
    aliens.add(alien)


def ship_hit(ai_settings, stats, screen, alien, aliens):
    """响应飞船被外星人撞到"""
    if stats.ships_left > 1:
        # 将ships_left减1
        stats.ships_left -= 1
        aliens.remove(alien)

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_alien(ai_settings, screen, aliens)

    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, aliens):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, alien, aliens)


def update_aliens(ai_settings, stats, screen, ship, aliens):
    """
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    """
    aliens.update()

    # 检查碰撞
    if pygame.sprite.spritecollide(ship, aliens, True):
        create_alien(ai_settings, screen, aliens)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, aliens)

    print(len(aliens))
