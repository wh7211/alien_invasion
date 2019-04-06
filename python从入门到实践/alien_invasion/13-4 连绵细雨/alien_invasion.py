#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

"""

13-4 连绵细雨：修改为完成练习 13-3 而编写的代码，使得一行雨滴消失在屏幕底端后，屏幕顶端又出现一行新雨滴，并开始往下落。

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
        gf.update_aliens(ai_settings, aliens, screen)
        gf.update_screen(ai_settings, screen, aliens)


run_game()
