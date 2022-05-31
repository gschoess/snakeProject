#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SnakeElement import SnakeElement


class Snake(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.head = SnakeElement(300, 300, 1, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav')
        self.add(self.head)  # initial Snake with three elements moving to the right
        self.add(SnakeElement(290, 300, 1, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        self.add(SnakeElement(280, 300, 1, 0, 'media/images/snake_tile.png', 10, 10, 'media/sounds/pain.wav'))
        # TODO Update Snake elements when new added
        self.snake_elements = self.sprites()
        print(type(self.snake_elements[0]))

    def turn(self, dir_x, dir_y):
        self.head.set_dir(dir_x, dir_y)

    def follow_head(self):
        for i in range(0, len(self.snake_elements)):
            if type(self.snake_elements[i]) == SnakeElement:
                pass
                # print("SnakeElement")
                # self.snake_elements[i].set_dir(1, 0)
                # self.sprites()[i].rect.left = self.sprites()[i-1].rect.left
                # self.sprites()[i].rect.top = self.sprites()[i-1].rect.top
                # first = snake_elements[i].__class__ = SnakeElement
                # dir_x_prev = self.snake_elements[i-1].get

    def update(self):
        pass

    def move(self):
        pass

    def grow(self):
        pass

    def detect_collission(self):
        pass
