#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SnakeElement import SnakeElement


class Snake(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.add(SnakeElement(300, 300, 1, 0, '../images/snake_tile.png', 10, 10, '../sounds/pain.wav'))  # initial Snake with three elements moving to the right
        self.add(SnakeElement(290, 300, 1, 0, '../images/snake_tile.png', 10, 10, '../sounds/pain.wav'))
        self.add(SnakeElement(280, 300, 1, 0, '../images/snake_tile.png', 10, 10, '../sounds/pain.wav'))

    def update(self):
        pass

    def move(self):
        pass

    def grow(self):
        pass

    def detect_collission(self):
        pass
