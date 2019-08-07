#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_DOWN:
        ship.moving_bottom = True
    elif event.key == pygame.K_UP:
        ship.moving_top = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_DOWN:
        ship.moving_bottom = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False


def check_events(ai_settings, screen, stats, play_button, ship, alien, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, ship,
                    alien, bullets, mouse_x, mouse_y)


def check_play_button(stats, play_button, ship, alien,
        bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 清空外星人列表和子弹列表
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        alien.y = alien.rect.height
        ship.center_ship()



def update_screen(ai_settings, screen, stats, ship, alien, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 绘制飞船
    ship.blitme()

    # 在屏幕上绘制编组中的每个外星人
    alien.blitme()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(stats, ship, alien, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.right >= ship.screen_rect.right:
            mark_stats(stats)
            bullets.remove(bullet)
    # print(len(bullets))

    check_bullet_alien_collisions(alien, bullets)



def check_bullet_alien_collisions(alien, bullets):
    """响应子弹和外星人的碰撞"""
    if pygame.sprite.spritecollideany(alien, bullets):
        alien_hit(alien, bullets)



def alien_hit(alien, bullets):
    """响应飞船被外星人撞到"""

    # 清空外星人列表和子弹列表
    bullets.empty()
    alien.y = alien.rect.height

    # 暂停
    sleep(0.5)


def mark_stats(stats):
    """响应飞船被外星人撞到"""
    if stats.alien_left > 0:
        # 将ships_left减1
        stats.alien_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_alien(ai_settings, alien):
    """
    检查是否有外星人到达屏幕边缘
      然后更新所有外星人的位置
    """

    if alien.check_edges():
        """将整群外星人下移，并改变它们的方向"""
        ai_settings.fleet_direction *= -1
    alien.update()

