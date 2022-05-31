#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class SnakeBodyElement(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y, image, scale_x, scale_y, sound):
        super().__init__(x, y, dir_x, dir_y, image, scale_x, scale_y, sound)

    def update(self):
        pass

    def move(self, x, y):
        self.rect.left = x
        self.rect.top = y

    def set_dir(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
