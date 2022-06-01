#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class SnakeHead(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y, image, scale_x, scale_y, sound):
        super().__init__(x, y, dir_x, dir_y, image, scale_x, scale_y, sound)
        self.moving = False  # necessary attribut to disallow start moving against direction when snake at rest

    def update(self):
        if self.moving:
            self.rect.left += self.dir_x * self.rect.width
            self.rect.top += self.dir_y * self.rect.height
