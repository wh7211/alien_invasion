#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

"""

# 13-3 雨滴：寻找一幅雨滴图像，并创建一系列整齐排列的雨滴。让这些雨滴往下落，直到到达屏幕底端后消失。

"""


import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf



def run_game():

    # 初始化pygame、设置和屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、一个用于存储子弹的编组和一个用于存储外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)


    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, aliens)


run_game()
