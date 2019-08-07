#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-


"""

12-1 蓝色天空：创建一个背景为蓝色的 Pygame 窗口。

"""

import pygame

from settings import Settings
import game_functions as gf


def run_game():

    # 初始化pygame、设置和屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:

        gf.check_events()
        gf.update_screen(ai_settings, screen)

run_game()