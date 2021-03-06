#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class FoodElement(SpriteElement):
    def __init__(self, game):
        super().__init__(0, 0, 0, 0, 'media/images/apple.png', game.el_size,
                         game.el_size, 'media/sounds/apple_bite.ogg')
        self.image.set_colorkey(pygame.Color("black"))
        self.set_to_random_pos(game.window)
