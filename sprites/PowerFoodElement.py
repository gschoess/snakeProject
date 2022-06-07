#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame.time

from sprites.SpriteElement import SpriteElement


class PowerFoodElement(SpriteElement):
    def __init__(self, game):
        super().__init__(0, 0, 0, 0, 'media/images/banana.png', game.el_size,
                         game.el_size, 'media/sounds/apple_bite.ogg')
        self.set_to_random_pos(game.window)
        self.game = game
        self.time = None
        self.LIFETIME = 10000  # ten seconds until the banana disappears

    def update(self):
        if self.time is not None:  # timer will be started in game loop
            # after lifetime is over, kill the sprite
            if pygame.time.get_ticks() - self.time >= self.LIFETIME:
                self.kill()
                self.game.create_food()
