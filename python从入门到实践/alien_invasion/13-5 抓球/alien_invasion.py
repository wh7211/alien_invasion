#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

"""

13-5 抓球：创建一个游戏，在屏幕底端放置一个玩家可左右移动的角色。让一个球出现在屏幕顶端，且水平位置是随机的，并让这个球以固定的速度往下落。
如果角色与球发生碰撞（表示将球抓住了），就让球消失。每当角色抓住球或球因抵达屏幕底端而消失后，都创建一个新球。

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
