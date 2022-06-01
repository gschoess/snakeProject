#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame

from sprites.SnakeHead import SnakeHead
from sprites.SnakeBodyElement import SnakeBodyElement


class Snake(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        # HEAD
        self.head = SnakeHead(300, 300, 1, 0, 'media/images/snake_head.png', 10, 10, 'media/sounds/pain.wav')
        self.add(self.head)

        # BODY
        self.body_elements = []
        self.body_elements.append(SnakeBodyElement(290, 300, 1, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        self.body_elements.append(SnakeBodyElement(280, 300, 1, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        self.body_elements.append(SnakeBodyElement(270, 300, 1, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        self.body_elements.append(SnakeBodyElement(260, 300, 1, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))

        # Add body elements to sprite group (Snake) for c
        for sprite in self.body_elements:
            self.add(sprite)

    def turn(self, dir_x, dir_y):
        self.head.set_dir(dir_x, dir_y)
        self.head.moving = True

    """
    Move the BodyElement to the Place of its Predecessor
    """
    def follow_head(self):
        self.body_elements[0].set_new_pos(self.head.rect.left, self.head.rect.top)
        for i in range(1, len(self.body_elements)):
            self.body_elements[i].set_new_pos(self.body_elements[i-1].rect.left, self.body_elements[i-1].rect.top)

    def add_element(self):
        pass

    def update(self):
        pass

    def grow(self):
        pass

    def detect_collission(self):
        pass
