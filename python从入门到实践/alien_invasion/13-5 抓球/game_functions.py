#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

import sys
import pygame
from alien import Alien
from random import randint



def check_keydown_events(event, ai_settings, screen):
    """响应按键"""
    if event.key == pygame.K_q:
        sys.exit()


def check_events(ai_settings, screen):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen)


def update_screen(ai_settings, screen, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)


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


def update_aliens(ai_settings, aliens):
    """
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    """
    aliens.update()

    # 删除已消失的雨滴
    for alien in aliens.copy():
        if alien.rect.bottom >= ai_settings.screen_height:
            aliens.remove(alien)
    # print(len(aliens))