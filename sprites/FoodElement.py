#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class FoodElement(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y):
        self.image = pygame.image.load('../images/snake_tile.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.sound = pygame.mixer.Sound("../sounds/pain.wav")
        SpriteElement.__init__(self, x, y, dir_x, dir_y, self.image, self.sound)
