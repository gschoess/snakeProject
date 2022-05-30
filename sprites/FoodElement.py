#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class FoodElement(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y, image, scale_x, scale_y, sound):
        super().__init__(x, y, dir_x, dir_y, image, scale_x, scale_y, sound)

