#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800

        # 将屏幕背景色设置为该图像的背景色
        self.bg_color = (255, 255, 255)