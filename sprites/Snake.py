#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SnakeElement import SnakeElement


class Snake(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.add(SnakeElement(300, 300, 1, 0))  # initial Snake with three elements moving to the right
        self.add(SnakeElement(290, 300, 1, 0))
        self.add(SnakeElement(280, 300, 1, 0))

    def update(self):
        pass
