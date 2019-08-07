#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-


"""

14-1 按 P 开始新游戏：鉴于游戏《外星人入侵》使用键盘来控制飞船，最好让玩
家也能够通过按键来开始游戏。请添加让玩家在按 P 时开始游戏的代码。也许这样做会
有所帮助：将 check_play_button()的一些代码提取出来，放到一个名为 start_game()
的函数中，并在 check_play_button()和 check_keydown_events()中调用这个函数。

"""

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf



def run_game():

    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")


    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)


    # 创建一艘飞船、一个用于存储子弹的编组和一个用于存储外星人的编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)



    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
                bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                play_button)


run_game()
