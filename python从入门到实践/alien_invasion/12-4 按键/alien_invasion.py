#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

"""

12-4 按键：创建一个程序，显示一个空屏幕。在事件循环中，每当检测到pygame.KEYDOWN 事件时都打印属性 event.key。运行这个程序，并按各种键，看看 Pygame如何响应。

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

        gf.check_events(ai_settings)
        gf.update_screen(ai_settings, screen)

run_game()