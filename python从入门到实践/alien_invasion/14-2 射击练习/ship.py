#!/usr/local/python365/bin/python3
# -*- coding:utf-8 -*-

import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形

        self.image = pygame.image.load('../../images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # 将每艘新飞船放在屏幕底部中央
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # 在飞船的属性center中存储小数值
        self.center_y = float(self.rect.centery)

        # 移动标志
        self.moving_bottom = False
        self.moving_top = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            if self.moving_bottom:
                self.center_y += self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            if self.moving_top:
                self.center_y -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centery = self.center_y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

