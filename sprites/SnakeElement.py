#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class SnakeElement(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y, image, scale_x, scale_y, sound):
        super().__init__(x, y, dir_x, dir_y, image, scale_x, scale_y, sound)

    def update(self):
        self.rect.left += self.dir_x * self.scale_x
        self.rect.top += self.dir_y * self.scale_y

    def set_dir(self, dir_x, dir_y):
        self.dir_x += dir_x * self.scale_x
        self.dir_y += dir_y * self.scale_y