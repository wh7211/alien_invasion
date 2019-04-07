#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

"""

13-6 游戏结束：在为完成练习 13-5 而编写的代码中，跟踪玩家有多少次未将球接着。在未接着球的次数到达三次后，结束游戏。

"""


import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():

    # 初始化pygame、设置和屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、一个用于存储子弹的编组和一个用于存储外星人的编组

    ship = Ship(ai_settings, screen)
    aliens = Group()



    # 创建外星人群
    gf.create_alien(ai_settings, screen, aliens)



    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_aliens(ai_settings, screen, ship, aliens)
        gf.update_screen(ai_settings, screen, aliens, ship)


run_game()
