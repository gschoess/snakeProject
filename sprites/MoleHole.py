#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class MoleHole(SpriteElement):
    def __init__(self, game):
        super().__init__(0, 0, 0, 0, 'media/images/mole_hole.png',
                         game.el_size, game.el_size,
                         'media/sounds/dig.wav')
        self.image.set_colorkey(pygame.Color("white"))
        self.connected_hole = None
        while True:
            self.set_to_random_pos(game.window)
            if not pygame.sprite.spritecollide(self, game.body_sg, False):
                break

    def set_connected_hole(self, mole_hole):
        self.connected_hole = mole_hole
