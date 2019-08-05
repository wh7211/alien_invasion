#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-


"""

14-3 有一定难度的射击练习：以你为完成练习 14-2 而做的工作为基础，让标靶的
移动速度随游戏进行而加快，并在玩家单击 Play 按钮时将其重置为初始值。

"""



import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():

    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Shooting")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    alien = Alien(ai_settings, screen)



    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, alien, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(stats, ship, alien, bullets)
            gf.update_alien(ai_settings, alien)
        gf.update_screen(ai_settings, screen, stats, ship, alien, bullets, play_button)

run_game()
