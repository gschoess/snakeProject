#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pygame
from sprites.SpriteElement import SpriteElement


class SnakeHead(SpriteElement):
    def __init__(self, x, y, dir_x, dir_y, snake):
        super().__init__(x, y, dir_x, dir_y, 'media/images/snake_head.png', 10, 10, 'media/sounds/pain.wav')
        self.snake = snake
        self.moving = False  # necessary attribut to disallow start moving against direction when snake at rest

    def update(self):
        if self.moving:
            self.snake.body_follow_head()
            self.rect.left += self.dir_x * self.rect.width
            self.rect.top += self.dir_y * self.rect.height

