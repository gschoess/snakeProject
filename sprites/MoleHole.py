#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime
from random import randint

import pygame
from sprites.SpriteElement import SpriteElement


class MoleHole(SpriteElement):
    def __init__(self, game):
        super().__init__(0, 0, 0, 0, 'media/images/mole_hole.png', game.el_size, game.el_size, 'media/sounds/apple_bite.wav')
        self.image.set_colorkey(pygame.Color("white"))  # White color will not be blit.
        self.connected_hole = None
        self.set_to_random_pos(game.window)

    def set_connected_hole(self, mole_hole):
        self.connected_hole = mole_hole
