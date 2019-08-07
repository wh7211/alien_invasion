#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

"""

12-3 火箭：编写一个游戏，开始时屏幕中央有一个火箭，而玩家可使用四个方向键上下左右移动火箭。请务必确保火箭不会移到屏幕外面。

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
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()