#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-


"""

12-2 游戏角色：找一幅你喜欢的游戏角色位图图像或将一幅图像转换为位图。创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，或将屏幕背景色设置为该图像的背景色。

"""

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():

    # 初始化pygame、设置和屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:

        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()