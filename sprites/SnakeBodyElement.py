#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class SnakeBodyElement(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y, image, scale_x, scale_y, sound):
        super().__init__(x, y, dir_x, dir_y, image, scale_x, scale_y, sound)

    """
    set_new_pos(). Notwendig da die Signatur der pygame.sprites.update()-Methode Sprites nicht geändert werden kann.
    Spricht keine Übergabe von Parametern möglich.
    """
    def set_new_pos(self, x, y):
        self.new_pos_x = x
        self.new_pos_y = y

    def update(self):
        self.rect.left = self.new_pos_x
        self.rect.top = self.new_pos_y
