#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

"""

13-2 更逼真的星星：为让星星的分布更逼真，可随机地放置星星。本书前面说过，可像下面这样来生成随机数：

***
from random import randint
random_number = randint(-10,10)
***

上述代码返回一个-10和10之间的随机整数。在为完成练习 8-6 而编写的程序中，随机地调整每颗星星的位置。

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
        gf.update_screen(ai_settings, screen, aliens)


run_game()
