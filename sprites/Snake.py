#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame

from sprites.SnakeHead import SnakeHead
from sprites.SnakeBodyElement import SnakeBodyElement
from sprites.SnakeElement import SnakeElement


class Snake(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.head = SnakeHead(300, 300, 0, 0, 'media/images/snake_head.png', 10, 10, 'media/sounds/pain.wav')
        # self.prevHead = []
        self.add(self.head)

        self.body_elements = []
        self.body_elements.append(SnakeBodyElement(290, 300, 0, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        self.body_elements.append(SnakeBodyElement(280, 300, 0, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        self.body_elements.append(SnakeBodyElement(270, 300, 0, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        self.body_elements.append(SnakeBodyElement(260, 300, 0, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))

        for sprite in self.body_elements:
            self.add(sprite)

    def turn(self, dir_x, dir_y):
        self.head.set_dir(dir_x, dir_y)

    """
    Move the BodyElement to the Place of its Predecessor
    """
    def follow_head(self):
        self.body_elements[0].move(self.head.rect.left, self.head.rect.top)
        for i in range(len(self.body_elements)-1, -1, -1):
            self.body_elements[i].move(self.body_elements[i-1].rect.left, self.body_elements[i-1].rect.top)

    def add_element(self):
        pass

    def update(self):
        pass

    def move(self):
        pass

    def grow(self):
        pass

    def detect_collission(self):
        pass
